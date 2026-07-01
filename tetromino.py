import pygame
from color import Colors

class pos:                                    # this was orignally in position.py but i thought it would be better 
    def __init__(self, row, column):          # to group the lode logically with tetromino and it reduced game a file size making it efficient.
        self.row = row
        self.column = column

    def __repr__(self):
        return f"pos(row={self.row}, column={self.column})"


class tetromino:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_change = 0
        self.column_change = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, rows, columns):
        self.row_change += rows
        self.column_change += columns
    
    def get_positions_of_cell(self): # important
        tiles = self.cells[self.rotation_state]
        moved_tiles = []

        for tile in tiles:
            moved_tile = pos(
                tile.row + self.row_change,
                tile.column + self.column_change
            )
            moved_tiles.append(moved_tile)

        return moved_tiles
    
    def rotate(self):  # cycles through rotations 
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def reverse_rotation(self):    # does similar to previous movement and restrict rotation outside grid.
        self.rotation_state -= 1  # this part is completed btw
        if self.rotation_state < 0:
            self.rotation_state = len(self.cells)  - 1
    
    def draw(self, screen, change_x, change_y):
        tiles = self.get_positions_of_cell()
        color = self.colors[self.id]
        for tile in tiles:
            x = tile.column * self.cell_size + change_x
            y = tile.row * self.cell_size + change_y
            size = self.cell_size - 1
            tile_rect = pygame.Rect(x, y, size, size)
            pygame.draw.rect(screen, color, tile_rect)
