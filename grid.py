import pygame
class Grid:
    def __init__(self):
        self.num_row = 20
        self.num_col = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_col)] for i in range(self.num_row)]
        self.colors = self.get_cell_color()
    def print_grid(self):
        for row in range(self.num_row):
            for column in range(self.num_col):
                print(self.grid[row][column], end="")
            print()
    def get_cell_color(self):
        dark_grey = (26, 31, 41)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234 , 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)
        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]
    def draw(self, screen):
        for row in range(self.num_row):
            for column in range(self.num_col):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(
                    column * self.cell_size +1,row * self.cell_size +1,self.cell_size -1,self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)