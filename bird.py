import pygame
from settings import BIRD_IMGS, BIRD_SIZE, BIRD_VELOCITY, BIRD_ANGLE, BIRD_X, BIRD_Y

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = BIRD_IMGS[0]
        self.rect = self.image.get_rect(topleft=(BIRD_X, BIRD_Y))
        self.index = 0
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up:
            self.rect.y -= BIRD_VELOCITY
            self.index = (self.index + 1) % len(BIRD_IMGS)
            self.image = BIRD_IMGS[self.index]
        if self.moving_down:
            self.rect.y += BIRD_VELOCITY
            self.index = (self.index + 1) % len(BIRD_IMGS)
            self.image = BIRD_IMGS[self.index]
