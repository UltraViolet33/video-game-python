import pygame
import sys
from Player import Player
from Enemy import Enemy
from Fire import Fire
from Topscore import Topscore
from Limit import Limit

pygame.init()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
FPS = 20

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

ADD_NEW_FIRE_RATE = 25

CLOCK = pygame.time.Clock()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Basic Video Game")
font = pygame.font.SysFont('forte', 20)

topscore = Topscore()


def game_loop():
    print('ok')
    while True:
        global enemy
        enemy = Enemy()
        global limit_top
        limit_top = Limit(0, 0)
        global limit_bottom
        limit_bottom = Limit(0, 599)
        fire = Fire(enemy)
        player = Player()
        add_new_fire_counter = 0
        fires_list = []
        global SCORE
        SCORE = 0
        global HIGH_SCORE
        while True:
            window.fill(BLACK)
            check_level(SCORE)
            enemy.update(window, limit_top, limit_bottom)
            add_new_fire_counter += 1

            if add_new_fire_counter == ADD_NEW_FIRE_RATE:
                add_new_fire_counter = 0
                new_fire = Fire(enemy)
                fires_list.append(new_fire)

            for fire in fires_list:
                if fire.fire_img_rect.left < 0:
                    fires_list.remove(fire)
                    SCORE += 1
                fire.update(window)
            print('o')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.up = True
                        player.down = False
                    elif event.key == pygame.K_DOWN:
                        player.down = True
                        player.up = False

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        player.up = False
                        player.down = True
                    elif event.key == pygame.K_DOWN:
                        player.down = True
                        player.up = False

            score_font = font.render("Score: " + str(SCORE), True, GREEN)
            score_font_rect = score_font.get_rect()
            score_font_rect.center = (200, score_font_rect.height/2)
            window.blit(score_font, score_font_rect)

            level_font = font.render("Level: " + str(LEVEL), True, GREEN)
            level_font_rect = level_font.get_rect()
            level_font_rect.center = (500, score_font_rect.height/2)
            window.blit(level_font, level_font_rect)
            
            top_score_font = font.render("Top Score: " + str(topscore.high_score), True, GREEN)
            top_score_rect = top_score_font.get_rect()
            top_score_rect.center = (800, score_font_rect.height/2)
            window.blit(top_score_font, top_score_rect)

            limit_top.update(window)
            limit_bottom.update(window)
            player.update(window)

            for fire in fires_list:
                if fire.fire_img_rect.colliderect(player.player_img_rect):
                    game_over()

            if player.check_collision_limuits(limit_top, limit_bottom):
                game_over()

            pygame.display.update()
            CLOCK.tick(FPS)


def game_over():
    topscore.top_score(SCORE)
    font = pygame.font.SysFont('forte', 50)

    game_over_font = font.render("Game over ! ", True, RED)
    game_over_rect = game_over_font.get_rect()
    game_over_rect.center = (600, 300)
    window.blit(game_over_font, game_over_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                game_loop()
        pygame.display.update()


def start_game():
    window.fill(BLACK)
    font = pygame.font.SysFont('forte', 50)

    game_title_font = font.render("Basic Game using Pygame", True, GREEN)
    game_title_rect = game_title_font.get_rect()
    game_title_rect.center = (600, 300)
    window.blit(game_title_font, game_title_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.update()


def check_level(SCORE):
    global LEVEL
    global limit_top
    global limit_bottom
    if SCORE in range(0, 5):
        LEVEL = 1
    elif SCORE in range(6, 20):
        limit_top.y = 50
        limit_bottom.y = 550
        LEVEL = 2
    elif SCORE in range(20, 30):
        limit_top.y = 100
        limit_bottom.y = 500
        LEVEL = 3
    elif SCORE > 30:
        limit_top.y = 200
        limit_bottom.y = 400
        LEVEL = 4


start_game()
