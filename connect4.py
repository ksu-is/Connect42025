import numpy as np

def initialize_board():
  return np.zeros((6, 7), dtype=int)

def is_move_valid(board, column, player):
  return board[0][column] == 0

def drop_piece(board, column, player):
  for row in range(5, -1, -1):
    if board[row][column] == 0:
      board [row][column] = player
      return True
  return False

def check_win(board, player):
 
  for row in range(6):
      for column in range(4):
            if all(board[row][column:column+4] == player):
                return True


for row in range(3):
        for column in range(7):
            if all(board[row:row+4, column] == player):
                return True

    for row in range(3):
        for column in range(4):
            if all(np.diag(board[row:row+4, column:column+4]) == player):
                return True

    for row in range(3, 6):
        for column in range(4):
            if all(np.diag(np.fliplr(board[row-3:row+1, column:column+4])) == player):
                return True
    return False

def print_board(board):
    for row in board:
        print("|" + "|".join(map(str, row)) + "|")
