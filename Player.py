import pygame

class Player:
    def __init__(self):
        self.player_img = pygame.image.load("./assets/player.png")
        self.player_img_rect = self.player_img.get_rect()
        self.player_img_rect.left = 20
        self.player_img_rect.top = 200
        self.down = True
        self.up = False
        self.velocity = 10
        
    
    def update(self, window):
        window.blit(self.player_img, self.player_img_rect)
        if self.up:
            self.player_img_rect.top -= 10
        if self.down:
            self.player_img_rect.bottom += 10
        