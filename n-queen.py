import random
from datetime import datetime

# Creating the board in a list where each value represents the number of the row it is present and it's index represents the column number.
def create_board(board_size):
	board = range(0,board_size)
	return board

# Randomising the queens
def randomise_queens(board):
	for i in range(0,len(board)):
		board[i] = random.randint(0,len(board)-1)
