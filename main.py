import pygame
import sys
from play import *
from color import Colors
from tetromino import tetromino,pos

pygame.init()
head_font = pygame.font.Font(None, 40)
scr_surface = head_font.render(" Score", True , Colors.white)  # score text value
next_surface = head_font.render(" Next Block", True , Colors.white)  # next block's text value
game_over_surface = head_font.render("GAME OVER", True, Colors.white)  # game over message display when user looses

scr_rec = pygame.Rect(320, 55, 170, 60)          # positions for the rectangles to place changing score value
next_rect = pygame.Rect(320, 215, 170, 180)      # same like for score but thsi for the next block(kinda makes the game little easier)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("TETRIS 2.0")   # cool name - mom
clock = pygame.time.Clock()

play = Play()
paused = False  # this is to pause the game

UPDATE_THE_GAME = pygame.USEREVENT
pygame.time.set_timer(UPDATE_THE_GAME, 200) #Changed it 24th march (Number value decreases = speed of game increases and vice versa)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if play.game_over:
                print("Restarting The game........,")
                play.game_over = False
                play.reset_play_state()

                 # this help to pause the game and resume it when u just click any key
            elif event.key == pygame.K_p and not play.game_over:
                paused = True
            elif paused:
                paused = False  # any other key resumes

            # Normal controls (only if not paused)  - check coursework movement page
            elif not paused:
                if event.key == pygame.K_LEFT:
                    play.go_left()
                elif event.key == pygame.K_RIGHT:
                    play.go_right()
                elif event.key == pygame.K_DOWN:
                    play.go_down()
                    play.increase_score(0,1)
                elif event.key == pygame.K_UP:
                    play.rotation()
        # block falls gradually(automatically) through the time value mentioned earlier 
        if event.type == UPDATE_THE_GAME and play.game_over == False and not paused:
            play.go_down()
    # Drawing
    surface_score_value = head_font.render(str(play.game_score), True, Colors.white)
    screen.fill(Colors.dark_blue)
    screen.blit(scr_surface, (356,20,50,50))
    screen.blit(next_surface, (330,180,50,50))
    if play.game_over:
        screen.blit(game_over_surface, (320,450,50,50))
    pygame.draw.rect(screen, Colors.light_blue, scr_rec, 0, 10)
    screen.blit(surface_score_value, surface_score_value.get_rect(centerx = scr_rec.centerx, centery = scr_rec.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    play.draw(screen)

    # this will display the game is paused overlay --- "PAUSED"
    if paused:
        paused_surface = head_font.render("PAUSED", True, Colors.white)
        screen.blit(paused_surface, (320, 400))

    pygame.display.update()
    clock.tick(60)   # frames

