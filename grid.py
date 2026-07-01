import pygame
from color import Colors
class Grid:
    def __init__(self):
        self.num_row = 20
        self.num_col = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_col)] for i in range(self.num_row)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_row): 
            for column in range(self.num_col):
                print(self.grid[row][column], end="")
            print()

    def is_inside(self, row, column): #def block_inside_grid(self) uses this to check
        if row < 0 or row >= self.num_row:
            return False
        if column < 0 or column >= self.num_col: # row column checked
            return False
        return True
    
    def is_blank(self, row, column):
        cell_value = self.grid[row][column]  # get the value of the cell and check if its empty
        if cell_value == 0:                   
            result = True                     
        else:
            result = False                    #
        return result    

    def is_row_completed(self, row):
        column = 0
        while column < self.num_col:
            if self.grid[row][column] == 0:
                return False
            column = column + 1
        return True


    def row_cleared(self, row):
        column = 0
        while column < self.num_col:
            self.grid[row][column] = 0
            column = column + 1


    def move_the_row_down(self, row, num_rows):
        column = 0
        new_row = row + num_rows

        while column < self.num_col:
            self.grid[new_row][column] = self.grid[row][column]
            self.grid[row][column] = 0
            column = column + 1


    def check_clear_full_rows(self):
        completed = 0
        row = self.num_row - 1

        while row >= 0:
            if self.is_row_completed(row):
                self.row_cleared(row)
                completed = completed + 1
            else:
                if completed > 0:
                    self.move_the_row_down(row, completed)
            row = row - 1

        return completed

    def draw(self, screen):
        for row in range(self.num_row):
            for column in range(self.num_col):
                cell_value = self.grid[row][column]  # get the value at this cell
                cell_rect = pygame.Rect(
                    column * self.cell_size + 11,  #  the x position of on screen
                    row * self.cell_size + 11,     # y position if the screen
                    self.cell_size - 1,            # width of the cell and its height aswell.
                    self.cell_size - 1             )
                # draw rectanlgular with the correct color i want.
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

    def restart_game(self):
        row = 0
        while row < self.num_row:                         # iteration
            column = 0
            while column < self.num_col:
                self.grid[row][column] = 0                # i set each cell to 0 to show empty space
                column = column + 1
            row = row + 1