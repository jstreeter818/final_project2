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
    return board[5][col] == 0


def get_next_open_row(board, col):
    for i in range(row_count):
        if board[i][col] == 0:
            return i


def print_board(board):
    print(np.flip(board, 0))


board = create_board()
print_board(board)
game_over = False
turn = 0

# main game loop
while not game_over:
    if turn == 0:
        col = int(input("PLayer 1, make your selection(0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

    else:
        col = int(input("PLayer 2, make your selection(0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

    print_board(board)

    turn += 1
    turn = turn % 2
