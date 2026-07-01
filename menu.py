import pygame
import sys
import subprocess
from switch import Button     

pygame.init()

WIDTH, HEIGHT = 500, 620 # this sets the game window
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) # pixel width and height for the game winfow
pygame.display.set_caption("TETRIS 2.0") # title for game

BACKGROUND = pygame.image.load("assets_for_menu/Background.png")
loading_SCREEN = pygame.image.load("assets_for_menu/loading.png")   
# thses both load assets from the asset folder/file to run background image and etc


def load_font1(size):
    # added wrapper for font1 to centralise   font changes
    return pygame.font.Font("assets_for_menu/font.ttf", size)# font number 1

#  liked these 2 fonts so i used them both as font1 and font2
def load_font2(size):
    return pygame.font.Font("assets_for_menu/font2.ttf", size) # font number 2


def loading_screen():
    #created the loading screen which will loop and ask for inputs enter or spacebar to move on it acts as palceholder before actual menu
    title_font = load_font2(75)                                                      # this would be the function for initial loading screen
    title_text = title_font.render("TETRIS", True, "white")
    title_rect = title_text.get_rect(center=(WIDTH // 2, 100))

    prompt_font = load_font1(27)
    prompt_text = prompt_font.render("PRESS ENTER/SPACEBAR TO CONTINUE", True, "white")   # conditions needed to pass through loading screen
    prompt_rect = prompt_text.get_rect(center=(WIDTH // 2, 410))

    while True:
        SCREEN.fill("black") # screen color defaulted to BLACK
        SCREEN.blit(loading_SCREEN, (0, 0))
        SCREEN.blit(title_text, title_rect)
        SCREEN.blit(prompt_text, prompt_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):  # when key press is correct , proceeds to main menu
                    return

        pygame.display.update()  # updates the display 


def instructions_screen():                     # this is to educate the user on how to play the game(navigate)
    while True:
        mouse_pos = pygame.mouse.get_pos()
        SCREEN.fill("black")                      # i first filled the screen black to then display message (simple)

        lines = [
            "HOW TO PLAY:",
            "",                                                   # actual instruction itself
            "← →   Move piece left / right",
            "↑      Rotate piece",
            "↓      Soft drop (fall faster)",
            "P - Pauses/Any Key To Resume",
            "Clear full horizontal lines to score points.",
            "The game ends when the Block reaches top."
        ]

        font = load_font1(23)
        y_offset = 150               # helps to position the text and more importantly vertical spacing increases redability without straining player

        for line in lines:                                                                   
            text = font.render(line, True, "white")
            SCREEN.blit(text, text.get_rect(center=(WIDTH // 2, y_offset)))  
            y_offset += 40
               
        back_btn = Button(None, (WIDTH // 2, 520), "BACK", load_font1(50), "white", "green")            # this is the back button which updates the SCREEN if clicked
        back_btn.update_color(mouse_pos) # back button uses the buttom class from switch file
        back_btn.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #to make it smoother , the quit is consistant across all screens. 
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_btn.check_click(mouse_pos):             # this is control for back button which is just mouse click
                                                                # and user is returned to main menu
                    return

        pygame.display.update()


def scores_screen(): # i just added this method recently since i didnt have time to fully do score table for tetris (had to complete evaluation!)
    while True:
        mouse_pos = pygame.mouse.get_pos()
        SCREEN.fill("black")
        #  the Title
        title_font = load_font2(60)
        title_text = title_font.render("SCORES", True, "white")  # title at the top of screen
        SCREEN.blit(title_text, title_text.get_rect(center=(WIDTH // 2, 100)))
        # Placeholder text (explains feature not ready becuase i didnt have time and to be replaced by HIGH SCORE SYSTEM!)
        info_font = load_font1(25)
        info_lines = [
            "High Score system is currently",
            "under development.",                           # message to user that its under development stil
            "",
            "Coming in the next update!"]
        y_offset = 250
        for line in info_lines:                                                # displays the messsages by iterating it through each line
            text = info_font.render(line, True, "white")
            SCREEN.blit(text, text.get_rect(center=(WIDTH // 2, y_offset))) # positions the text
            y_offset += 40
        # Back button 
        back_btn = Button(None, (WIDTH // 2, 520), "BACK", load_font1(50), "white", "green")  # back button logic
        back_btn.update_color(mouse_pos)  # hover logic(color changes when hovered over it)
        back_btn.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:   # control 
                if back_btn.check_click(mouse_pos):
                    return
        pygame.display.update()

def main_menu():                   # this is the method for main menu that will hold all options to go to
    while True:   # this is the main menu loop  where each button is positioned o nagivate
        mouse_pos = pygame.mouse.get_pos()

        SCREEN.blit(BACKGROUND, (0, 0))

        title = load_font2(51).render("MAIN MENU", True, "#ffffff") # the title of course
        SCREEN.blit(title, title.get_rect(center=(250, 100))) # menu title
        # buttoms for each option is made sure to highlight when hovered over.
        play_btn = Button(None, (250, 240), "PLAY", load_font1(50), "#1C1CB7E2", "white")   # this will rediret player to main.py and run it since thas the game 
        scr_btn = Button(None, (250, 330), "SCORES", load_font1(50), "#1C1CB7E2", "white") # score button which opens the placeholder now
        inst_btn = Button(None, (250, 420), "INSTRUCTIONS", load_font1(50), "#1C1CB7E2", "white") # button for instructions
        quit_btn = Button(None, (250, 510), "QUIT", load_font1(50), "#1C1CB7E2", "white") # a dedicated quit button to safely exit if needed

        for btn in (play_btn, scr_btn, inst_btn, quit_btn):          # this i made it so color of buttons changes when hovered over them which is cool
            btn.update_color(mouse_pos) #hover logic 
            btn.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                       # this is when quit button is pressed the game just ends , game window terminated
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_btn.check_click(mouse_pos):                             # when play is clicked for sately i wrote a print statement to let user know the game is ran 
                    print("PLAY CLICKED")        # i got the subprocess feature from online which would redirect and run main.py which is the game , but it helps with debugging and isolating aspects of game easily
                    pygame.quit()                                                   
                    subprocess.run(["py", r"main.py"])
                    sys.exit()

                if scr_btn.check_click(mouse_pos):
                    scores_screen()                                             # was: print("Scores clicked") before until now i changed to the scores screen method to hold the placehodler 
  

                if inst_btn.check_click(mouse_pos):   # instruction screen
                    instructions_screen()  # opens the score placeholder mentioned above

                if quit_btn.check_click(mouse_pos): # quit button logic
                    pygame.quit()
                    sys.exit()   # ability to quit cleanl from main menu through a button at end right below instructions

        pygame.display.update() # displays updated


loading_screen()
main_menu()



class treasure:
    def __init__(self, value, level):
        self.__value = value
        self.__level = level
        