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

# initialize size and color of the board
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
    DISPLAYSURF.fill(background_color)
    pygame.display.set_caption('Memory Puzzle')

    mainboard = getIconBoard()
    drawBoard(mainboard)
    reveal_Board = revealBoard()

    mouseClicked = False
    firstBox = None

    while True:
        for event in pygame.event.get(): #handling event
            if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        col, row = getBoxAtCoordinate(mousex, mousey)
        if col != None and row != None:
            if not isRevealed(col, row, reveal_Board):
                highlightBox(col, row)
            if not isRevealed(col, row, reveal_Board) and mouseClicked:
                reveal_Board[row][col] = True
                if firstBox == None:
                    firstBox = [mainboard[row][col], (col, row)]
                else:
                    secondBox = [mainboard[row][col], (col, row)]
                    if secondBox[0][0] != firstBox[0][0] or secondBox[0][1] != firstBox[0][1]:
                        reveal_Board[firstBox[1][1]][firstBox[1][0]] = False
                        reveal_Board[secondBox[1][1]][secondBox[1][0]] = False

                        # cover first box and this box
                    # if they match and the game is not end, dont do anything
                    # if the game end, celebrate user
                    elif endGame(reveal_Board):
                        endGameAnimation()

        pygame.display.update()
        fpsClock.tick(FPS)


def generateBoard():
    boxx = x_margin + gapsize//2
    for row in range(board_width):
        boxy = y_margin + gapsize//2
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

def drawBox(col, row, revealSpeed, icon_board):
    left, top = getLeftTop(col, row)
    pygame.draw.rect(DISPLAYSURF, box_color, (left, top, boxsize, boxsize))
    color, icon = icon_board[row][col]
    right = left + boxsize
    bottom = top + boxsize
    half = boxsize // 2
    # draw icon
    if icon == RING:
        pygame.draw.ellipse(DISPLAYSURF, color, (left + 10, top + 10, 40, 40), 5)
    elif icon == CROSS:
        pygame.draw.line(DISPLAYSURF, color, (left + 10, top + 10), (right - 10, bottom - 10), 5)
        pygame.draw.line(DISPLAYSURF, color, (left + 10, bottom - 10), (right - 10 , top + 10), 5)
    elif icon == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left + 10, top + 10, 40, 40))
    elif icon == CIRCLE:
        pygame.draw.ellipse(DISPLAYSURF, color, (left + 10, top + 10, 40, 40))
    elif icon == TRIANGLE:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top + 10), (left + 10, bottom - 10), (right - 10, bottom - 10)))
    elif icon == DIAMOND:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top + 10), (left + 10, top + half), (left + half, bottom - 10), (right - 10, top + half)))


def drawBoard(icon_board):
    revealSpeed = 0
    for row in range(board_height):
        for col in range(board_width):
            drawBox(col, row, revealSpeed, icon_board)

def revealBoard():
    revealed = []
    for _ in range(board_height):
        add = [False]*board_width
        revealed.append(add)
    return revealed

def isRevealed(col, row, board):
    return board[row][col]

# def getCoverBox():

def highlightBox(col, row):
    left, top = getLeftTop(col, row)
    pygame.draw.rect(DISPLAYSURF, BLUE1, (left, top, boxsize, boxsize), 6)

# get position of left and top of box
def getLeftTop(col, row):
    left = x_margin + gapsize // 2 + col * (boxsize + gapsize)
    top = y_margin + gapsize // 2 + row * (boxsize + gapsize)
    return (left, top)

def getBoxAtCoordinate(x,y):
    for row in range(board_height):
        for col in range(board_width):
            left, top = getLeftTop(col, row)
            boxRect = pygame.Rect(left, top, boxsize, boxsize)
            if boxRect.collidepoint(x,y):
                return (col, row)
    return (None, None)

def endGame(revealBoard):
    return all(all(x == True for x in row) for row in revealBoard)

def endGameAnimation():
    pygame.draw.rect(DISPLAYSURF, (255, 255, 255, 0.6), (0, 0, width, height))
    endingFont = pygame.font.sysFont('Helvetica', 60)
    for color in color_set:
        textSurfaceObj = endingFont.render('YOU WIN!', True, color, None)
        textRect = textSurfaceObj.get_rect()
        textRect.center = (width//2 , height//2)
        pygame.display.update()
        pygame.time.wait(200)


if __name__ == '__main__':
    main()
