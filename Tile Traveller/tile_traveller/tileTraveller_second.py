# GitHub repo # GitHub repo https://github.com/ermir18/ru_assignments/blob/master/tile_traveller/tileTraveller_second.py
"""
1)In the beginning of the assignment, i thought the first implementation would be easier,
and sure it was, but after i finished my second implementation, i learned a lot about functions,
returning values, sending values etc.
2) I think the second implementation is a little more readable because it is wrapped
in functions, before knowing how functions work for me it would be more difficult to read
but now it is easier.
3)Both my implementations have very similar logic behind, in second implementation i don't
have to limit the high and lower values, becauese my function will take care to only increment
or decrease the value if it will get the right direction.
"""
"""
First i decide that i am going to use two coordinates to track the user position, in x and y
then i define two constansts that my user cannot bo above and below
then i declare a boolean value to check the selection of the user if it is a valid,
another boolean that is going to be false unless the user has made it to the victory tile
"""

x = 1
y = 1
#LOW = 1
#HIGH = 3
valid_selection = True
break_of_prog = False


def printing(print_x, print_y):
	"""
	This function will print possibility that the user have to move
	in a certain position.
	"""
	if print_x == 1 and print_y == 1:
		print("You can travel: (N)orth.")
	elif print_x == 1 and print_y == 2:
		print("You can travel: (N)orth or (E)ast or (S)outh.")
	elif print_x == 1 and print_y == 3:
		print("You can travel: (E)ast or (S)outh.")
	elif print_x == 2 and print_y == 1:
		print("You can travel: (N)orth.")
	elif print_x == 2 and print_y == 2:
		print("You can travel: (S)outh or (W)est.")
	elif print_x == 2 and print_y == 3:
		print("You can travel: (E)ast or (W)est.")
	elif print_x == 3 and print_y == 3:
		print("You can travel: (S)outh or (W)est.")
	elif print_x == 3 and print_y == 2:
		print("You can travel: (N)orth or (S)outh.")
	else:
		print("Victory!")


def position(pos_choice, print_x, print_y, valid, func_break):
	"""
	This function will get a value that the user will choose, value from the printed x and printed y,
	from the printing() function, value of the valid selection and value of the break of function.
	if the the user makes a certain choice than the program will either increase or decreasy x or y;
	or it will print that it is not a valid direction, a trick to stop the loop before it checks
	at the position 3,1, if the user is at the position 3,2 and chooses to move south, then 
	break of program will turn true and when the while loop will check for the next value and will halt the program with Victory!
	"""
	if print_x == 1 and print_y == 1:
		if pos_choice.lower() == "n":
			return print_x, print_y + 1, True, False
		else:
			print("Not a valid direction!")
			return print_x, print_y, False, False
	elif print_x == 1 and print_y == 2:
		if pos_choice.lower() == "n":
			return print_x, print_y + 1, True, False
		elif pos_choice.lower() == "e":
			return print_x + 1, print_y, True, False
		elif pos_choice.lower() == "s":
			return print_x, print_y - 1, True, False
		else:
			print("Not a valid direction!")
			return print_x, print_y, False, False
	elif print_x == 1 and print_y == 3:
		if pos_choice.lower() == "e":
			return print_x + 1, print_y, True, False
		elif pos_choice.lower() == "s":
			return print_x, print_y - 1, True, False
		else:
			print("Not a valid direction!")
			return print_x, print_y, False, False
	elif print_x == 2 and print_y == 1:
		if pos_choice.lower() == "n":
			return print_x, print_y + 1, True, False
		else:
			print("Not a valid direction!")
			return print_x, print_y, False, False
	elif print_x == 2 and print_y == 2:
		if pos_choice.lower() == "s":
			return print_x, print_y - 1, True, False
		elif pos_choice.lower() == "w":
			return print_x - 1, print_y, True, False
		else:
			print("Not a valid direction!")
			return print_x, print_y, False, False
	elif print_x == 2 and print_y == 3:
		if pos_choice.lower() == "e":
			return print_x + 1, print_y, True, False
		elif pos_choice.lower() == "w":
			return print_x + 1, print_y, True, False
		else:
			print("Not a valid direction!")
			return print_x, print_y, False, False
	elif print_x == 3 and print_y == 3:
		if pos_choice.lower() == "s":
			return print_x, print_y - 1, True, False
		elif pos_choice.lower() == "w":
			return print_x - 1, print_y, True, False
		else:
			print("Not a valid direction!")
			return print_x, print_y, False, False
	elif print_x == 3 and print_y == 2:
		if pos_choice.lower() == "s":
			print("Victory!")
			return print_x, print_y - 1, True, True
		elif pos_choice.lower() == "n":
			return print_x, print_y + 1, True, False
		else:
			print("Not a valid direction!")
			return print_x, print_y, False, False
	elif print_x == 3 and print_y == 1:
		return print_x, print_y, True, True


while break_of_prog == False:
	if valid_selection is True:
		printing(x, y)
	choice = input("Direction: ")
	x, y, valid_selection, break_of_prog = position(choice, x, y, valid_selection, break_of_prog)