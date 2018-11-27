def make_board(n):  # This makes the nested list
	list1 = [list(range(1 + n * i, 1 + n * (i + 1))) for i in range(n)]
	return list1


def draw_board(a_list):  # This draw the board with right just 5
	for i in a_list:
		i = [str(j).rjust(5) for j in i]
		print(" ".join(i))


def get_input(dime, player):
	"""
	This function converts the input into a coordinate [x][y] and also return false
	if the input is not a digit.
	"""
	# not_valid = False
	move_x = input("{} position: ".format(player))
	dime = int(dime)
	if not move_x.isdigit():
		return dime * 4, dime * 4, dime * 4, True
	else:
		return (int(move_x) - 1) // dime, (int(move_x) - 1) % dime, move_x, False


def illegal_move(a, b, move, valid):
	if int(move) - 1 >= dimension * dimension:
		return True
	if board[a][b] == "X" or board[a][b] == "O":
		return True


def modify_list(a, b, player):  # This function prints the board with the updated X or O
	board[a][b] = player
	return board


def win_game_x(n, x_board):  # This function check if the player X has won
	countx = 0
	county = 0
	for i in range(n):
		if x_board[i][i] == "X":  # Diagonal
			countx += 1
			if countx == n:
				return True
		if x_board[i][n - (i + 1)] == "X":
			county += 1
			if county == n:
				return True

	for i in range(n):
		countz = 0
		for j in range(n):  # Horizontal
			if x_board[i][j] == "X":  # 0,0 0,1 0,2
				countz += 1
				if countz == n:
					return True

	for i in range(n):
		countb = 0  # Vertical check
		for j in range(n):
			if x_board[j][i] == "X":  # 0,0 1,0 2,0
				countb += 1
				if countb == n:
					return True
	else:
		return False


def draw_game(n, d_board):  # This function checks if the game is Draw.
	count = 0
	elements = n * n
	for i in range(n):
		for j in range(n):
			if d_board[i][j] == "X" or d_board[i][j] == "O":
				count += 1
			if count == elements:
				return True


def win_game_y(n, y_board):
	""" This function check if the player O has won, i know this could be done in one step and
	with less code but, maybe i will refactor in another project, because i have way too much to do for all 4 classes"""
	count_x = 0
	count_y = 0
	for i in range(n):
		if y_board[i][i] == "O":  # Diagonal
			count_x += 1
			if count_x == n:
				return True
		if y_board[i][n - (i + 1)] == "O":  # or board[i][n - (i + 1)] == "O":
			count_y += 1
			if count_y == n:
				return True

	for i in range(n):
		count_z = 0
		for j in range(n):  # Horizontal
			if y_board[i][j] == "O":  # 0,0 0,1 0,2
				count_z += 1
				if count_z == n:
					return True

	for i in range(n):
		count_b = 0  # Vertical check
		for j in range(n):
			if y_board[j][i] == "O":  # 0,0 1,0 2,0
				count_b += 1
				if count_b == n:
					return True
	else:
		return False


def signing(dimension, board, draw, player):  # This function checks if it is a illegal move.
	a, b, move, valid = get_input(dimension, player)
	if illegal_move(a, b, move, valid):
		print("Illegal move!")
		draw = False
	else:
		modify_list(a, b, player)
		draw = True
	return draw


# #----------------Main program starts here---------------# #

dimension = int(input("Input dimension of the board: "))
#dimension = 3
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
	if win_game_x(dimension, board):
		draw_board(board)
		print("Winner is: X")
		victory = True
	if win_game_y(dimension, board):
		draw_board(board)
		print("Winner is: O")
		victory = True
	if draw_game(dimension, board):
		draw_board(board)
		print("Draw!")
		victory = True
