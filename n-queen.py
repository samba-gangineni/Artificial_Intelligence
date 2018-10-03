import random
import time

# Creating the board in a list where each value represents the number of the row it is present and it's index represents the column number.
def create_board(board_size):
	board = range(0,board_size)
	return board

# Randomising the queens
def randomise_queens(board):
	for i in range(0,len(board)):
		board[i] = random.randint(0,len(board)-1)
	return board

# Calculating the conflicts
def conflict(row,col,board):
	conflicts = 0
	for i in range(0,len(board)):
		if i != col:
			next_queen = board[i]
			if next_queen == row or abs(next_queen - row) == abs(i-col):
				conflicts+=1
	return conflicts


# Solving the board

def solve(board_size):
	board = randomise_queens(create_board(board_size))
	moves = 0
	candidates = []
	while True:
		# Finding the queen with the maximum conflict
		max_conflict = 0
		candidates = []
		for i in range(0,board_size):
			conflicts = conflict(board[i],i,board)
			if conflicts == max_conflict:
				candidates.append(i)
			elif conflicts > max_conflict:
				max_conflict = conflicts				
				candidates = []
				candidates.append(i)

		# If all the queens are checked and we dont have nany conflicts
		if max_conflict==0:
			print"number of moves: {}".format(moves)
			return board

		# There might be many queens with maximum conflicts, hence picking one
		max_conflict_queen = candidates[random.randint(0,len(candidates)-1)]


		#moving the queen to a row with minimum conflict
		min_conflict = board_size
		candidates = []
		for j in range(0,board_size):
			conflicts = conflict(j,max_conflict_queen,board)
			if conflicts == min_conflict:
				candidates.append(j)

			elif conflicts < min_conflict:
				min_conflict = conflicts
				candidates=[]
				candidates.append(j)

		# Changing the queen into the row where there is minimum conflict
		if not len(candidates)==0:
			board[max_conflict_queen] = candidates[random.randint(0,len(candidates)-1)]

		# As we have moved on piece increase the count
		moves+=1

		# Printing the board
		print_board(board)
		if moves > 2*board_size:
			print "Starting over again"
			board = randomise_queens(board)
			moves = 0


def print_board(board):
	row = ''
	for i in range(0,len(board)):
		for j in range(0,len(board)):
			if board[j] == i:
				row+="Q "
			else:
				row+="_ "

		row+="\n"
	print row



def main():
	start_time = time.time()
	start = True
	while(start):
		try:
			board_size = int(input("How many columns in the board?"))
			board = solve(board_size)
			print_board(board)
			print "Total time: {} seconds".format(time.time()-start_time)

			start = False
		except ValueError as ex:
			print "Oops! Please enter a valid integer. Try again."		

if __name__ =="__main__":
	main()
	
