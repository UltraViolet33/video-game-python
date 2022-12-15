import pygame

class Fire:
    
    def __init__(self, enemy):
        self.fire_img = pygame.image.load("./assets/fire.jpg")
        self.fire_img = pygame.transform.scale(self.fire_img, (20, 20))
        self.fire_img_rect = self.fire_img.get_rect()
        self.fire_img_rect.right = enemy.enemy_img_rect.left
        self.fire_img_rect.top = enemy.enemy_img_rect.top + 30
        self.velocity = 20
        
    def update(self, window):
        window.blit(self.fire_img, self.fire_img_rect)
        
        if self.fire_img_rect.left > 0:
            self.fire_img_rect.left -= self.velocity
    