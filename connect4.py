import numpy as np

def initialize_board():
  return np.zeros((6, 7), dtype=int)

def is_move_valid(board, column, player):
  return board[0][column] == 0

def drop_piece(board, column, player):
  for row in range(5, -1, -1):
    if board[row][column] == 0:
      board [row][column] = player
