from allfunctions import *

#Put your sudoku board instead of mine
#Replace empty cells with 0
board = [
	[0, 0, 0, 0, 0, 0, 2, 0, 0],
	[0, 8, 0, 0, 0, 7, 0, 9, 0],
	[6, 0, 2, 0, 0, 0, 5, 0, 0],
	[0, 7, 0, 0, 6, 0, 0, 0, 0],
	[0, 0, 0, 9, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 2, 0, 0, 4, 0],
	[0, 0, 5, 0, 0, 0, 6, 0, 3],
	[0, 9, 0, 4, 0, 0, 0, 7, 0],
	[0, 0, 6, 0, 0, 0, 0, 0, 0]
]



print_board(board)
print("\n\n")
solve(board)
print("\n\n")
print_board(board)
input()