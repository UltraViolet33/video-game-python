import pygame


class Limit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 1200, 1), 2)
