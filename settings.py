import pygame
import os

# Screen settings
WIDTH, HEIGHT = 600, 800
FPS = 60

# Bird settings
BIRD_IMGS = [pygame.image.load(os.path.join('assets', 'bird1.png')),
             pygame.image.load(os.path.join('assets', 'bird2.png')),
             pygame.image.load(os.path.join('assets', 'bird3.png'))]
BIRD_IMGS = [img.convert_alpha() for img in BIRD_IMGS]
BIRD_Y = HEIGHT * 0.6
BIRD_X = WIDTH * 0.2
BIRD_SIZE = 60
BIRD_ANGLE = 0
BIRD_VELOCITY = 5

# Pipe settings
PIPE_GAP = 200
PIPE_VELOCITY = 4
PIPE_WIDTH = 70
PIPE_HEIGHT = 400
PIPE_IMAGE = pygame.image.load(os.path.join('assets', 'pipe.png'))
PIPE_IMAGE = PIPE_IMAGE.convert_alpha()

# Scoring
SCORE = 0
FONT = pygame.font.SysFont('comicsans', 50)
