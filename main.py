import pygame
import numpy as np
import math
import sys

row_count = 6
column_count = 7


def create_board():
    board = np.zeros((6,7))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[row_count - 1][col] == 0


def get_next_open_row(board, col):
    for i in range(row_count):
        if board[i][col] == 0:
            return i


def print_board(board):
    print(np.flip(board, 0))


def check_for_win(board, piece):
    # Check horizontal wins
    for c in range(column_count - 3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # Check vertical wins
    for c in range(column_count):
        for r in range(row_count - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # Check positive diagonal wins
    for c in range(column_count - 3):
        for r in range(row_count - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    # Check negative diagonal wins
    for c in range(column_count - 3):
        for r in range(3, row_count):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


board = create_board()
print_board(board)
game_over = False
turn = 0
winner = None

# main game loop
while not game_over:
    if turn == 0:
        col = int(input("PLayer 1, make your selection(0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
            if check_for_win(board, 1):
                game_over = True
                winner = 'Player 1'

    else:
        col = int(input("PLayer 2, make your selection(0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            if check_for_win(board, 2):
                game_over = True
                winner = 'Player 2'

    print_board(board)

    turn += 1
    turn = turn % 2

print(winner, 'won!')
