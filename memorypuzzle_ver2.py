import pygame, sys
import random
from pygame.locals import *

# color
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = ( 50, 200,  50)
NAVYBLUE = ( 60,  60, 180)
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
    mousex, mousey = 0, 0
    pygame.init()

    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((width, height))

    pygame.display.set_caption('Memory Puzzle')
    mainboard = getIconBoard()
    while True:
        mouseClicked = False

        DISPLAYSURF.fill(background_color)
        drawBoard(mainboard)

        for event in pygame.event.get(): #handling event
            if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        pygame.display.update()


def generateBoard():
    boxx = x_margin + gapsize/2
    for row in range(board_width):
        boxy = y_margin + gapsize/2
        for col in range(board_height):
            pygame.draw.rect(DISPLAYSURF, box_color, (boxx, boxy, boxsize, boxsize))
            boxy += (boxsize + gapsize)
        boxx += (boxsize + gapsize)

def getIconBoard():
    # create set of diffent figures with colors
    icons = []
    for color in color_set:
        for figure in figure_set:
            icons.append((color, figure))

    # randomly arrange the set
    random.shuffle(icons)
    num_of_box = int(board_width * board_height / 2)
    icons = icons[:num_of_box] * 2
    random.shuffle(icons)

    puzzle_board = []
    add = 0
    while add + board_width <= num_of_box * 2:
        row = icons[add:add + board_width]
        puzzle_board.append(row)
        add += board_width
    return puzzle_board

def drawBoard(icon_board):
    for row in range(board_height):
        for col in range(board_width):
            left, top = getLeftTop(col, row)
            pygame.draw.rect(DISPLAYSURF, box_color, (left, top, boxsize, boxsize))
            color, icon = icon_board[row][col]
            size_icon = boxsize - 20
            top_icon = top + 10
            left_icon = left + 10
            half = boxsize / 2
            # draw icon
            if icon == RING:
                pygame.draw.ellipse(DISPLAYSURF, color, (left_icon, top_icon, size_icon, size_icon), 5)
            elif icon == CROSS:
                pygame.draw.line(DISPLAYSURF, color, (left + 10, top + 10), (left + boxsize - 10, top + boxsize - 10), 5)
                pygame.draw.line(DISPLAYSURF, color, (left + 10, top + boxsize - 10), (left + boxsize - 10 , top + 10), 5)
            elif icon == SQUARE:
                pygame.draw.rect(DISPLAYSURF, color, (left_icon, top_icon, size_icon, size_icon))
            elif icon == CIRCLE:
                pygame.draw.ellipse(DISPLAYSURF, color, (left_icon, top_icon, size_icon, size_icon))
            elif icon == TRIANGLE:
                pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top_icon),
                (left_icon, top + 50), (left + boxsize - 10, top + 50)))
            elif icon == DIAMOND:
                pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top_icon), (left_icon, top + half),
                (left + half, top + boxsize - 10), (left + boxsize - 10, top + half)))

def getCoverBox():
    
# get position of left and top of box
def getLeftTop(boxx, boxy):
    left = x_margin + gapsize / 2 + boxx * (boxsize + gapsize)
    top = y_margin + gapsize / 2 + boxy * (boxsize + gapsize)
    return (left, top)

def getBoxAtCoordinate(x,y):
    for row in range(board_height):
        for col in range(board_width):
            left, top = getLeftTop(col, row)
            boxRect = pygame.Rect(left, top, boxsize, boxsize)
            if boxRect.collidepoint(x,y):
                return (col, row)
    return (None, None)



# def user_win():

if __name__ == '__main__':
    main()
