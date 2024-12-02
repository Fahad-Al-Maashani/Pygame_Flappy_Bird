import pygame
import sys
from settings import *
from bird import Bird
from pipe import Pipe

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

bird = Bird()
pipes = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(bird)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird.moving_up = True
    if keys[pygame.K_DOWN]:
        bird.moving_down = True

    bird.update()
    pipes.update()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
