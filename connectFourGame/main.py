# This is a sample connect four game.
import numpy as np
import pygame
import sys
import math

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0,0)
YELLOW = (255, 255, 0)
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE/2 -5)
WIDTH = COLUMN_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE
SIZE = (WIDTH, HEIGHT)


def print_board(board):
	print(np.flip(board, 0))


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(window, BLUE, (c * SQUARE_SIZE, (r + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(window, BLACK, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(window, RED, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(window, YELLOW, (
                int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

    pygame.display.update()


def is_free(board, col):
    return board[ROW_COUNT - 1][col] == 0


def drop_piece(board, row, col, piece):
    board[row][col] = piece

def get_drop_row(board, col):
    for r in range(ROW_COUNT):
        if board[ROW_COUNT- r -1][col] == 0:
            return ROW_COUNT - r - 1


def winner(board, player):
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] ==player and board[r][c + 1] == player and board[r][c + 2] == player and board[r][c + 3] == player:
                return True

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
                return True
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return True
    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == player and board[r - 1][c + 1] == player and board[r - 2][c + 2] == player and board[r - 3][c + 3] == player:
                return True
    return False


board = create_board()
game_over = False
turn = 0
print(board)

pygame.init()

window = pygame.display.set_mode(size=SIZE)
draw_board(board)
pygame.display.update()


myfont = pygame.font.SysFont("monospace", 75)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(window, BLACK, (0, 0, WIDTH, SQUARE_SIZE))
            posx = event.pos[0]

            if turn == 0:
                pygame.draw.circle(window, RED, (posx, int(SQUARE_SIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(window, YELLOW, (posx, int(SQUARE_SIZE / 2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(window, BLACK, (0, 0, WIDTH, SQUARE_SIZE))

            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARE_SIZE))

                if is_free(board, col):
                    row = get_drop_row(board, col)
                    drop_piece(board, row, col, turn + 1)
                    if winner(board, turn + 1):
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        window.blit(label, (40, 10))
                        game_over = True

            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARE_SIZE))

                if is_free(board, col):
                    row = get_drop_row(board, col)
                    drop_piece(board, row, col, turn + 1)

                    if winner(board, turn + 1):
                        label = myfont.render("Player 2 wins!!", 2, RED)
                        window.blit(label, (40, 10))
                        game_over = True

        draw_board(board)
        print_board(board)
        turn += 1
        turn = turn % 2
