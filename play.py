from grid import Grid
import random  
from tetrominos import Lblock, Jblock, Oblock, Iblock, Sblock, Tblock, Zblock  
from tetromino import tetromino,pos


class Play:
    def __init__(self):
        self.grid = Grid()   # initialised the grid , nextblock , currnet block and block sets so that later i can use them through gameplay
        self.blocks = [Lblock(), Jblock(), Oblock(), Iblock(), Sblock(), Tblock(), Zblock()]
        self.active_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.game_score = 0

    # add method for score here:  
    def increase_score(self, lines_cleared, down_points):  #  17/03/26 , this list is what i shown in coursework, score per line along with scores for each ;)
        score_values = {1: 100, 2: 300, 3: 500}
        if lines_cleared in score_values:
            self.game_score += score_values[lines_cleared]
        self.game_score +=  down_points

    def get_random_block(self):
        if len(self.blocks) == 0:  # ramdomises the block and gets a first block and next block to select and then remove from the actual list after use and then randomise list again when all blocks run out.
            self.blocks = [Lblock(), Jblock(), Oblock(), Iblock(), Sblock(), Tblock(), Zblock()]  
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def block_can_fit(self):                             
        return self.block_can_fit_block(self.active_block)

    def block_can_fit_block(self, block): ## checks if one block overlaps the other and if it fits
        tiles = block.get_positions_of_cell()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
            if not self.grid.is_blank(tile.row, tile.column):
                return False
        return True

    def block_inside_grid(self): ## this works now 
        tiles = self.active_block.get_positions_of_cell()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True

    def fix_block(self):                                                                ### lock blocks into the grid. # lcok block
        tiles = self.active_block.get_positions_of_cell()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.active_block.id
        if not self.block_can_fit_block(self.next_block):
            self.game_over = True
            return  
        self.active_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.check_clear_full_rows()
        self.increase_score(rows_cleared, 0)

    def go_left(self):    # minor bug . coordinate accdeintally set to +1 previously when it should have -1 instead (0, -1)
        self.active_block.move(0, -1)
        if not self.block_inside_grid() or not self.block_can_fit():
            self.active_block.move(0, 1)

    def go_right(self):
        self.active_block.move(0, 1)
        if not self.block_inside_grid() or not self.block_can_fit():
            self.active_block.move(0, -1)

    def go_down(self):
        self.active_block.move(1, 0)
        if not self.block_can_fit():
            self.active_block.move(-1, 0)  # Undo move
            self.fix_block()               # Lock block and spawn next

    def rotation(self):
        self.active_block.rotate()
        if not self.block_inside_grid() or not self.block_can_fit():
            self.active_block.reverse_rotation()

    def draw(self, screen):                                           
        self.grid.draw(screen)
        self.active_block.draw(screen, 11, 11)
        self.next_block.draw(screen, 270, 270)
        # bug fix: well i updated draw() method signature caused TypeError due to cached version
        # solution i  cleared cache / restarted program so new method (with offsets) is used

    def reset_play_state(self):
        self.grid.restart_game()        
        self.blocks = [Lblock(), Jblock(), Oblock(), Iblock(), Sblock(), Tblock(), Zblock()]
        block = self.get_random_block()
        self.active_block = block
        block = self.get_random_block()
        self.next_block = block
        self.game_score = 0

