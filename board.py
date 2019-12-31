import pygame
from cell import cell
from pathfinder import Astar

WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
BLACK=(0,0,0)


class board():
    def __init__(self, board_size, game_height, game_width, line_colour = (255, 255, 255)):
        self.board_size = board_size
        self.passable = True;
        self.game_height = game_height
        self.game_width = game_width
        self.path_finder = Astar(self)

        self.cells = [[cell(x, y) for y in range(board_size[1])] for x in range(board_size[0])]

    def get_path(self, start, end):
        print(end)
        return self.path_finder.find_path(self.cells[start[0]][start[0]], self.cells[end[0]][end[1]])

    def set_passable(self, x, y, passable):
        self.cells[x][y].set_passable(passable)

    def get_cell_neighbours(self, x, y):
        neighbours = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                print(i, j)
                if i > 0 and i < self.board_size[0] and j > 0 and j < self.board_size[1]:
                    if self.cells[i][j].passable and not (x == i and y == j):
                        neighbours.append(self.cells[i][j])
        return neighbours

    def reset_board(self):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                self.cells[i][j].checked = False

    def draw(self, surface):
        for x in range(self.board_size[0]):
            for y in range(self.board_size[1]):
                if self.cells[x][y].checked:
                    pygame.draw.rect(surface, GREEN, (x * (self.game_width / self.board_size[0]), y * (self.game_height / self.board_size[1]), (self.game_width / self.board_size[0]), (self.game_height / self.board_size[1])))
                elif self.cells[x][y].passable:
                    pygame.draw.rect(surface, BLUE, (x * (self.game_width / self.board_size[0]), y * (self.game_height / self.board_size[1]), (self.game_width / self.board_size[0]), (self.game_height / self.board_size[1])))

        for x in range(self.board_size[0] + 1):
            pygame.draw.line(surface, BLACK, (x * (self.game_width / self.board_size[0]) , 0), (x * (self.game_width / self.board_size[0]), self.game_height))

        for y in range(self.board_size[1]):
            pygame.draw.line(surface, BLACK, (0, y * (self.game_height / self.board_size[1])), (self.game_width, y * (self.game_height / self.board_size[1])))
