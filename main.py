import pygame, sys, math, board
from pygame.locals import *


pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 400))
GAME_WIDTH, GAME_HEIGHT = pygame.display.get_surface().get_size()
NUM_CELLS = (20, 20)
WHITE=(255,255,255)
BLUE=(0,0,255)
BLACK=(0,0,0)

pygame.display.set_caption('A*')

board = board.board(NUM_CELLS, GAME_HEIGHT, GAME_WIDTH)
print(board)

def get_mouse_pos_index():
    x , y = pygame.mouse.get_pos()
    x = math.floor(x / (GAME_WIDTH / NUM_CELLS[0]))
    y = math.floor(y / (GAME_HEIGHT / NUM_CELLS[1]))
    return x, y


while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if pygame.mouse.get_pressed()[0]:
            try:
                x, y = get_mouse_pos_index()
                board.set_passable(x, y, False)
            except AttributeError:
                pass

        if pygame.mouse.get_pressed()[2]:
            try:
                board.reset_board()
                x, y = get_mouse_pos_index()
                #board.set_passable(x, y, False)

                path = board.get_path((0,0), (x,y))

                for cell in path:
                    cell.checked = True

            except AttributeError:
                pass


    DISPLAYSURF.fill(WHITE)

    #print(get_mouse_pos_index())
    board.draw(DISPLAYSURF)
    pygame.display.update()
