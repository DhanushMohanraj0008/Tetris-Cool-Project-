# import pygame
# import sys
# from switch import Button
# pygame.init()
# WIDTH, HEIGHT = 500, 620
# SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("TETRIS")
# BACKGROUND = pygame.image.load("assets_for_menu/Background.png")
# loading_SCREEN = pygame.image.load("assets_for_menu/loading.png")
# def load_font1(size):
#     return pygame.font.Font("assets_for_menu/font.ttf", size)
# def load_font2(size):
#     return pygame.font.Font("assets_for_menu/font2.ttf", size)
# def loading_screen():
#     title_font = load_font2(75)
#     title_text = title_font.render("TETRIS", True, "white")
#     title_rect = title_text.get_rect(center=(WIDTH // 2, 100))
#     prompt_font = load_font1(27)
#     prompt_text = prompt_font.render("PRESS ENTER/SPACEBAR TO CONTINUE", True, "white")
#     prompt_rect = prompt_text.get_rect(center=(WIDTH // 2, 410))
#     while True:
#         SCREEN.fill("black")
#         SCREEN.blit(loading_SCREEN, (0, 0))
#         SCREEN.blit(title_text, title_rect)
#         SCREEN.blit(prompt_text, prompt_rect)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key in (pygame.K_RETURN, pygame.K_SPACE):
#                     return
#         pygame.display.update()
# def play_screen():
#     while True:
#         mouse_pos = pygame.mouse.get_pos()
#         SCREEN.fill("black")
#         message = load_font1(45).render("This is the PLAY screen.", True, "white")
#         SCREEN.blit(message, message.get_rect(center=(WIDTH // 2, 260)))
#         back_btn = Button(None, (WIDTH // 2, 460), "BACK", load_font1(50), "white", "green")
#         back_btn.update_color(mouse_pos)
#         back_btn.update(SCREEN)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 if back_btn.check_click(mouse_pos):
#                     return
#         pygame.display.update()
# def hscore_screen():
#     while True:
#         mouse_pos = pygame.mouse.get_pos()
#         SCREEN.fill("grey")
#         message = load_font1(39).render("This is the Score screen!", True, "black")
#         SCREEN.blit(message, message.get_rect(center=(WIDTH // 2, 260)))
#         back_btn = Button(None, (WIDTH // 2, 460), "BACK", load_font1(50), "black", "green")
#         back_btn.update_color(mouse_pos)
#         back_btn.update(SCREEN)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 if back_btn.check_click(mouse_pos):
#                     return
#         pygame.display.update()
# def instructions_screen():
#     while True:
#         mouse_pos = pygame.mouse.get_pos()
#         SCREEN.fill("black")
#         lines = [
#             "HOW TO PLAY:",
#             "",
#             "← →   Move piece left / right",
#             "↑      Rotate piece",
#             "↓      Soft drop (fall faster)",
#             "SPACE  Hard drop (instant place)",
#         "Clear full horizontal lines to score points.",
#         "The game ends when the stack reaches top."
# ]

#         font = load_font1(23)
#         y_offset = 150
#         for line in lines:
#             text = font.render(line, True, "white")
#             SCREEN.blit(text, text.get_rect(center=(WIDTH // 2, y_offset)))
#             y_offset += 40
#         back_btn = Button(None, (WIDTH // 2, 520), "BACK", load_font1(50), "white", "green")
#         back_btn.update_color(mouse_pos)
#         back_btn.update(SCREEN)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 if back_btn.check_click(mouse_pos):
#                     return
#         pygame.display.update()
# def main_menu():
#     while True:
#         mouse_pos = pygame.mouse.get_pos()
#         SCREEN.blit(BACKGROUND, (0, 0))
#         title = load_font2(51).render("MAIN MENU", True, "#ffffff")
#         SCREEN.blit(title, title.get_rect(center=(250, 100)))
#         play_btn = Button(None, (250, 240), "PLAY", load_font1(50), "#1C1CB7E2", "white")
#         scr_btn  = Button(None, (250, 330), "SCORES", load_font1(50), "#1C1CB7E2", "white")
#         inst_btn = Button(None, (250, 420), "INSTRUCTIONS", load_font1(50), "#1C1CB7E2", "white")
#         quit_btn = Button(None, (250, 510), "QUIT", load_font1(50), "#1C1CB7E2", "white")
#         for btn in (play_btn, scr_btn, inst_btn, quit_btn):
#             btn.update_color(mouse_pos)
#             btn.update(SCREEN)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 if play_btn.check_click(mouse_pos):
#                     play_screen()
#                 if scr_btn.check_click(mouse_pos):
#                     hscore_screen()
#                 if inst_btn.check_click(mouse_pos):
#                     instructions_screen()
#                 if quit_btn.check_click(mouse_pos):
#                     pygame.quit()
#                     sys.exit()
#         pygame.display.update()
# loading_screen()
# main_menu()


# import pygame
# import sys
# import subprocess
# from switch import Button
# pygame.init()
# WIDTH, HEIGHT = 500, 620
# SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("TETRIS")
# BACKGROUND = pygame.image.load("assets_for_menu/Background.png")
# loading_SCREEN = pygame.image.load("assets_for_menu/loading.png")
# def load_font1(size):
#     return pygame.font.Font("assets_for_menu/font.ttf", size)
# def load_font2(size):
#     return pygame.font.Font("assets_for_menu/font2.ttf", size)
# def loading_screen():
#     title_font = load_font2(75)
#     title_text = title_font.render("TETRIS", True, "white")
#     title_rect = title_text.get_rect(center=(WIDTH // 2, 100))
#     prompt_font = load_font1(27)
#     prompt_text = prompt_font.render("PRESS ENTER/SPACEBAR TO CONTINUE", True, "white")
#     prompt_rect = prompt_text.get_rect(center=(WIDTH // 2, 410))
#     while True:
#         SCREEN.fill("black")
#         SCREEN.blit(loading_SCREEN, (0, 0))
#         SCREEN.blit(title_text, title_rect)
#         SCREEN.blit(prompt_text, prompt_rect)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key in (pygame.K_RETURN, pygame.K_SPACE):
#                     return
#         pygame.display.update()
# def main_menu():
#     while True:
#         mouse_pos = pygame.mouse.get_pos()
#         SCREEN.blit(BACKGROUND, (0, 0))
#         title = load_font2(51).render("MAIN MENU", True, "#ffffff")
#         SCREEN.blit(title, title.get_rect(center=(250, 100)))
#         play_btn = Button(None, (250, 240), "PLAY", load_font1(50), "#1C1CB7E2", "white")
#         scr_btn  = Button(None, (250, 330), "SCORES", load_font1(50), "#1C1CB7E2", "white")
#         inst_btn = Button(None, (250, 420), "INSTRUCTIONS", load_font1(50), "#1C1CB7E2", "white")
#         quit_btn = Button(None, (250, 510), "QUIT", load_font1(50), "#1C1CB7E2", "white")
#         for btn in (play_btn, scr_btn, inst_btn, quit_btn):
#             btn.update_color(mouse_pos)
#             btn.update(SCREEN)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 if play_btn.check_click(mouse_pos):
#                     print("PLAY CLICKED")  # debug
#                     pygame.quit()
#                     subprocess.run(["py", r"C:\Users\pdhkm\OneDrive\Desktop\TETRIS\main.py"])
#                     sys.exit()
#                 if scr_btn.check_click(mouse_pos):
#                     print("Scores clicked")
#                 if inst_btn.check_click(mouse_pos):
#                     print("Instructions clicked")
#                 if quit_btn.check_click(mouse_pos):
#                     pygame.quit()
#                     sys.exit()

#         pygame.display.update()

# loading_screen()
# main_menu()

import pygame
import sys
import subprocess
from switch import Button
pygame.init()
WIDTH, HEIGHT = 500, 620
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TETRIS")
BACKGROUND = pygame.image.load("assets_for_menu/Background.png")
loading_SCREEN = pygame.image.load("assets_for_menu/loading.png")
def load_font1(size):
    return pygame.font.Font("assets_for_menu/font.ttf", size)
def load_font2(size):
    return pygame.font.Font("assets_for_menu/font2.ttf", size)
def loading_screen():
    title_font = load_font2(75)
    title_text = title_font.render("TETRIS", True, "white")
    title_rect = title_text.get_rect(center=(WIDTH // 2, 100))
    prompt_font = load_font1(27)
    prompt_text = prompt_font.render("PRESS ENTER/SPACEBAR TO CONTINUE", True, "white")
    prompt_rect = prompt_text.get_rect(center=(WIDTH // 2, 410))
    while True:
        SCREEN.fill("black")
        SCREEN.blit(loading_SCREEN, (0, 0))
        SCREEN.blit(title_text, title_rect)
        SCREEN.blit(prompt_text, prompt_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    return
        pygame.display.update()
def instructions_screen():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        SCREEN.fill("black")
        lines = [
            "HOW TO PLAY:",
            "",
            "← →   Move piece left / right",
            "↑      Rotate piece",
            "↓      Soft drop (fall faster)",
            "SPACE  Hard drop (instant place)",
            "Clear full horizontal lines to score points.",
            "The game ends when the stack reaches top."
        ]
        font = load_font1(23)
        y_offset = 150
        for line in lines:
            text = font.render(line, True, "white")
            SCREEN.blit(text, text.get_rect(center=(WIDTH // 2, y_offset)))
            y_offset += 40
        back_btn = Button(None, (WIDTH // 2, 520), "BACK", load_font1(50), "white", "green")
        back_btn.update_color(mouse_pos)
        back_btn.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_btn.check_click(mouse_pos):
                    return
        pygame.display.update()
def main_menu():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        SCREEN.blit(BACKGROUND, (0, 0))
        title = load_font2(51).render("MAIN MENU", True, "#ffffff")
        SCREEN.blit(title, title.get_rect(center=(250, 100)))
        play_btn = Button(None, (250, 240), "PLAY", load_font1(50), "#1C1CB7E2", "white")
        scr_btn  = Button(None, (250, 330), "SCORES", load_font1(50), "#1C1CB7E2", "white")
        inst_btn = Button(None, (250, 420), "INSTRUCTIONS", load_font1(50), "#1C1CB7E2", "white")
        quit_btn = Button(None, (250, 510), "QUIT", load_font1(50), "#1C1CB7E2", "white")
        for btn in (play_btn, scr_btn, inst_btn, quit_btn):
            btn.update_color(mouse_pos)
            btn.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_btn.check_click(mouse_pos):
                    print("PLAY CLICKED")
                    pygame.quit()
                    subprocess.run(["py", r"main.py"])
                    sys.exit()
                if scr_btn.check_click(mouse_pos):
                    print("Scores clicked")
                if inst_btn.check_click(mouse_pos):
                    instructions_screen()
                if quit_btn.check_click(mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
loading_screen()
main_menu()
