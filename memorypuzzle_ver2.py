import pygame, sys
from pygame.locals import *

# color
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
NAVYBLUE = ( 60,  60, 100)
PURPLE   = (255,   0, 255)
BLACK    = (  0,   0,   0)
color_set = (WHITE, RED, GREEN, NAVYBLUE, PURPLE, BLACK)
BLUE1    = (10 , 10 , 100)
YELLOW1  = (250, 210, 150)
WHITE1   = (230, 230, 220)

# figure
RING     = 'ring'
CROSS    = 'cross'
SQUARE   = 'square'
CIRCLE   = 'circle'
TRIANGLE = 'triangle'
DIAMOND  = 'diamond'
figure_set = (RING, CROSS, SQUARE, CIRCLE, TRIANGLE, DIAMOND)

# initialize the board
board_width  = 6
board_height = 4
cover_color = BLUE1
gapsize = 10
boxsize = 50
box_color = WHITE1

# interface size
x_margin = int(boxsize * 1.5)
y_margin = int(boxsize * 2)
width   = 2 * x_margin + board_width * (boxsize + gapsize)
height  = 2 * y_margin + board_height * (boxsize + gapsize)
background_color = YELLOW1
FPS = 30
reveal_speed = 8
assert len(color_set)*len(figure_set) >= board_width * board_height, ...
'Not enough figures to be put into boxes!'

pygame.init()
DISPLAYSURF = pygame.display.set_mode((width, height))
DISPLAYSURF.fill(background_color)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
