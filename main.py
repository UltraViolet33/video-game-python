import pygame
import sys
from Player import Player
from Enemy import Enemy
from Fire import Fire

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

pygame.display.set_caption("Mario Clone")


def game_loop():
    print('ok')
    while True:
        global enemy
        enemy = Enemy()
        fire = Fire(enemy)
        player = Player()
        add_new_fire_counter = 0
        fires_list = []
        while True:
            window.fill(BLACK)
            enemy.update(window)
            add_new_fire_counter += 1
            
            if add_new_fire_counter == ADD_NEW_FIRE_RATE:
                add_new_fire_counter = 0
                new_fire = Fire(enemy)
                fires_list.append(new_fire)

            for fire in fires_list:
                if fire.fire_img_rect.left < 0:
                    fires_list.remove(fire)
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
                
            player.update(window)
            pygame.display.update()
            CLOCK.tick(FPS)


def start_game():
    window.fill(BLACK)
    
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


start_game()