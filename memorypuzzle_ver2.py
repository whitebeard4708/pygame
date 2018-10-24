import pygame, sys
import random
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
YELLOW1  = (250, 215, 160)
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
gapsize = 20
boxsize = 60
box_color = WHITE1
assert (board_width * board_height) % 2 == 0, 'There is a odd number of boxes.'

# interface size
x_margin = int(boxsize * 1.5)
y_margin = int(boxsize * 2)
width   = 2 * x_margin + board_width * (boxsize + gapsize)
height  = 2 * y_margin + board_height * (boxsize + gapsize)
background_color = YELLOW1
FPS = 30
reveal_speed = 8
assert len(color_set)*len(figure_set) >= (board_width * board_height) / 2, ...
'Not enough figures to be put into boxes!'



def main():
    global fpsClock, DISPLAYSURF
    pygame.init()

    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((width, height))
    DISPLAYSURF.fill(background_color)
    pygame.display.set_caption('Memory Puzzle')

    # mainboard = getRandomizedBoard()

    while True:
        generateBoard()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


def generateBoard():
    boxx = x_margin + gapsize/2
    for row in range(board_width):
        boxy = y_margin + gapsize/2
        for col in range(board_height):
            pygame.draw.rect(DISPLAYSURF, box_color, (boxx, boxy, boxsize, boxsize))
            boxy += (boxsize + gapsize)
        boxx += (boxsize + gapsize)


def getRandomizedBoard():
    # create set of diffent figures with colors
    icons = []
    for color in color_set:
        for figure in figure_set:
            icons.append((color, figure))

    # randomly arrange the set
    random.shuffle(icons)
    num_of_box = int(board_width * board_height) / 2
    icons = icons[:num_of_box] * 2
    random.shuffle(icons)

    puzzle_board = []
    add = 0
    while add + board_width < num_of_box * 2:
        row = icons[add:add+board_width]
        puzzle_board.append(row)
    return puzzle_board




def drawBoard(board):
    boxy = y_margin + gapsize/2
    for row in range(board_height):
        boxy = x_margin + gapsize/2
        for col in range(board_width):
            pygame.draw.rect(DISPLAYSURF, box_color, (boxx, boxy, boxsize, boxsize))

            boxx += (boxsize + gapsize)
        boxy += (boxsize + gapsize)

if __name__ == '__main__':
    main()
