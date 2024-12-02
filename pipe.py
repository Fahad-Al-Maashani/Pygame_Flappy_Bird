import pygame
from settings import PIPE_IMAGE, PIPE_WIDTH, PIPE_HEIGHT, PIPE_GAP, PIPE_VELOCITY

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = PIPE_IMAGE
        self.rect = self.image.get_rect(midtop=(x, 0))
        self.velocity = PIPE_VELOCITY
        self.gap = PIPE_GAP

    def update(self):
        self.rect.y += self.velocity
        if self.rect.y > HEIGHT:
            self.rect.y = -PIPE_HEIGHT
