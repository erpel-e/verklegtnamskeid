def make_board(n):
	list1 = [list(range(1 + n * i, 1 + n * (i + 1))) for i in range(n)]
	return list1


def draw_board(a_list):
	for i in a_list:
		i = [str(j).rjust(5) for j in i]
		print("".join(i))


def get_input(dime, player):
	not_valid = False
	move_x = input("{} position: ".format(player))
	if not move_x.isdigit():
		return 0, 0, 0, True
	else:
		return (int(move_x) - 1) // dime, (int(move_x) - 1) % dime, move_x, False


def illegal_move(a, b, move, valid):
	if int(move) - 1 >= dimension * dimension:
		return True
	if board[a][b] == "X":  # or board[a][b] == "O":
		return True
	if move.isdigit() == valid:
		print("it is illegal")
		return True


def modify_list(a, b, player):
	board[a][b] = player
	return board


def win_game_x(n, x_player):
	for i in range(n):
		for j in range(n):
			if board[i][j] != x_player:
				break
		else:
			print("Winner is:", x_player)
			return True

"""
	countx = 0
	county = 0
	for i in range(len(x_board)):
		if x_board[i][i] == "X":  # Diagonal
			countx += 1
			if countx == n:
				return True
		if x_board[i][n - (i + 1)] == "X":  # or board[i][n - (i + 1)] == "O":
			county += 1
			if county == n:
				return True
	countz = 0
	for i in range(len(x_board)):
		for j in range(len(x_board)):
			if x_board[i][j] == "X":  # Horizontal
				countz += 1
				if countz == n:
					return True
		#else:
		#	return False

	countb = 0
	for i in range(len(x_board)):
		for j in range(len(x_board)):
			if x_board[j][i] == "X": # Vertical check
				countb += 1 # 0,0 0,1 0,2
				if countb == n:
					return True
	else:
		return False
"""
"""
def win_game_y(n, y_board):
	count_x = 0
	count_y = 0
	for i in range(len(y_board)):  # diagonal
		if y_board[i][i] == "O":
			count_x += 1
			if count_x == n:
				return True
		if y_board[i][n - (i + 1)] == "O":  # diagonal
			count_y += 1
			if count_y == n:
				return True

	count_x = 0
	count_y = 0
	for i in range(len(y_board)):
		for j in range(len(y_board)):
			if y_board[i][j] == "O":  # horizontal
				count_y += 1
				if count_y == n:
					return True
	count_x = 0
	count_y = 0


# else:
# pass
# return False

# for i in range(len(board)):
#	for j in range(len(board)):
#		if board[i][i+n-1] == "O": # or board[i][j] == "O":
#			count_x += 1
#			if count_x == n:
#				return True
#	else:
#		return False
"""


def signing(dimension, board, draw, player):
	a, b, move, valid = get_input(dimension, player)
	if illegal_move(a, b, move, valid):
		print("Illegal move!")
		draw = False
	else:
		modify_list(a, b, player)
		draw = True
	return draw


# #----------------Main program starts here---------------# #
# dimension = int(input("Input dimension of the board: "))
dimension = 3
board = make_board(dimension)
draw = True
victory = False
player1 = "X"
player2 = "O"
current_player = player1

while not victory:
	if draw:
		draw_board(board)
	draw = signing(dimension, board, draw, current_player)
	if draw:
		if current_player == player1:
			current_player = player2
		else:
			current_player = player1
	if win_game_x(dimension, current_player):
		draw_board(board)
		print("Winner is : X")
		victory = True
# if win_game_y(dimension, board):
#	draw_board(board)
#	print("Winner is: O")
#	victory = True
