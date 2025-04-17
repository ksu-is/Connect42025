import numpy as np

def initialize_board():
  return np.zeros((6, 7), dtype=int)

def is_move_valid(board, column, player):
  return board[0][column] == 0


