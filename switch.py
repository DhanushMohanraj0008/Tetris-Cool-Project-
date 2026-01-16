import pygame
class Button:
    def __init__(self, image, position, text, font, default_color, hover_color): 
        self.image = image
        self.x, self.y = position
        self.font = font
        self.text_value = text
        self.default_color = default_color
        self.hover_color = hover_color
        self.text_surface = font.render(text, True, default_color)
        if self.image is None:
            self.image = self.text_surface
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text_rect = self.text_surface.get_rect(center=(self.x, self.y))
    def update(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.text_surface, self.text_rect)
    def check_click(self, pos):
        return self.rect.collidepoint(pos)
    def update_color(self, mouse_pos): # mouse positions
        if self.rect.collidepoint(mouse_pos):
            new_color = self.hover_color
        else:
            new_color = self.default_color
        self.text_surface = self.font.render(self.text_value, True, new_color)





        


