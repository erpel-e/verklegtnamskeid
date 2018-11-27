NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'
total = 0
def move(direction, col, row):
	if direction == NORTH:
		row += 1
	elif direction == SOUTH:
		row -= 1
	elif direction == EAST:
		col += 1
	elif direction == WEST:
		col -= 1
	return(col, row)

def is_victory(col, row):
	return col == 3 and row == 1 # (3,1)

def coins(col, row):
	coin = 1
	if col == 1 and row == 2:
		return coin
	elif col == 2 and row == 2:
		return coin
	elif col == 2 and row == 3:
		return coin
	elif col == 3 and row == 2:
		return coin

def print_coin():
	coin_ch = input("Pull a lever (y/n): ")
	return coin_ch

def coin_choice(coin_ch,t):
	if coin_ch.lower() == "y":
		t += 1
		print("You received 1 coins, your total is now {}.".format(t))
	return t


def print_directions(directions_str):
	print("You can travel: ", end='')
	first = True
	for ch in directions_str:
		if not first:
			print(" or ", end='')
		if ch == NORTH:
			print("(N)orth", end='')
		elif ch == EAST:
			print("(E)ast", end='')
		elif ch == SOUTH:
			print("(S)outh", end='')
		elif ch == WEST:
			print("(W)est", end='')
		first = False
	print(".")

def find_directions(col, row):
	if col == 1 and row == 1:   # (1,1)
		valid_directions = NORTH
	elif col == 1 and row == 2: # (1,2)
		valid_directions = NORTH+EAST+SOUTH
	elif col == 1 and row == 3: # (1,3)
		valid_directions = EAST+SOUTH
	elif col == 2 and row == 1: # (2,1)
		valid_directions = NORTH
	elif col == 2 and row == 2: # (2,2)
		valid_directions = SOUTH+WEST
	elif col == 2 and row == 3: # (2,3)
		valid_directions = EAST+WEST
	elif col == 3 and row == 2: # (3,2)
		valid_directions = NORTH+SOUTH
	elif col == 3 and row == 3: # (3,3)
		valid_directions = SOUTH+WEST
	return valid_directions


def is_playing():
	play_ch = input("Play again (y/n): ")
	return play_ch

def play(play_ch,total,col,row):
	if play_ch.lower() == "y":
		t = 0
		col = 1
		row = 1
		return True, t, col, row
	if play_ch.lower == "n":
		t = 0
		return False, t, col, row

# The main program starts here
victory = False
row = 1
col = 1
playing = True
valid_directions = NORTH
print_directions(valid_directions)
coin = False
while playing:
	if victory:
		playing, total, col, row = play(is_playing(), total, col, row)
		print("You can travel: (N)orth.")
	direction = input("Direction: ")
	direction = direction.lower()

	if not direction in valid_directions:
		print("Not a valid direction!")
	else:
		col, row = move(direction, col, row)
		victory = is_victory(col, row)
		coin = coins(col, row)
		#playing = is_playing()
		if victory:
			print("Victory!")
			#playing, total, col, row = play(is_playing(), total, col, row)
		else:
			if coin:
				total = coin_choice(print_coin(), total)
			valid_directions = find_directions(col, row)
			print_directions(valid_directions)
