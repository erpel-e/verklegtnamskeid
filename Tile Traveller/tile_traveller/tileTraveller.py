# GitHub repo https://github.com/ermir18/ru_assignments/blob/master/tile_traveller/tileTraveller.py
"""
We initialize two variable x and y for coordinates in the tile map,
We see that we have 9 tiles so we need to make 9 checks for 
9 possible actions, in each action we define what possibilites we have to move,
and we run this in a while loop so it will always run to check in what position
the user is and what action we can perform in that particular position.
When the user is in the tile of the victory the program will print "Victory!" 
and hit Brake!

"""
x = 1
y = 1
valid_selection = True

while True:
    if x == 1 and y == 1:
        if valid_selection == True:
            print("You can travel: (N)orth.")
        valid_selection = True
        choice = input("Direction: ")
        if choice.lower() == "n":
            y += 1
        else:
            print("Not a valid direction!")
            valid_selection = False
    elif x == 1 and y == 2:
        if valid_selection == True:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        valid_selection = True
        choice = input("Direction: ")
        if choice.lower() == "n":
            y += 1
            #print(x, y)
        elif choice.lower() == "e":
            x += 1
            #print(x, y)
        elif choice.lower() == "s":
            y -= 1
            #print(x, y)
        else:
            print("Not a valid direction!")
            valid_selection = False
    elif x == 1 and y == 3:
        if valid_selection == True:
            print("You can travel: (E)ast or (S)outh.")
        valid_selection = True
        choice = input("Direction: ")
        if choice.lower() == "e":
            x += 1
            #print(x, y)
        elif choice.lower() == "s":
            y -= 1
            #print(x,y)
        else:
            print("Not a valid direction!")
            valid_selection = False
    elif x == 2 and y == 1:
        if valid_selection == True:
            print("You can travel: (N)orth.")
        valid_selection = True
        choice = input("Direction: ")
        if choice.lower() == "n":
            y += 1
            #print(x, y)
        else:
            print("Not a valid direction!")
            valid_selection = False
    elif x == 2 and y == 2:
        if valid_selection == True:
            print("You can travel: (S)outh or (W)est.")
        valid_selection = True
        choice = input("Direction: ")
        if choice.lower() == "w":
            x -= 1
            #print(x, y)
        elif choice.lower() == "s":
            y -= 1
            #print(x,y)
        else:
            print("Not a valid direction!")
            valid_selection = False
    elif x == 2 and y == 3:
        if valid_selection == True:
            print("You can travel: (E)ast or (W)est.")
        valid_selection = True
        choice = input("Direction: ")
        if choice.lower() == "e":
            x += 1
            #print(x, y)
        elif choice.lower() == "w":
            x -= 1
            #print(x,y)
        else:
            print("Not a valid direction!")
            valid_selection = False
    elif x == 3 and y == 3:
        if valid_selection == True:
            print("You can travel: (S)outh or (W)est.")
        valid_selection = True
        choice = input("Direction: ")
        if choice.lower() == "w":
            x -= 1
            #print(x, y)
        elif choice.lower() == "s":
            y -= 1
            #print(x,y)
        else:
            print("Not a valid direction!")
            valid_selection = False
    elif x == 3 and y == 2:
        if valid_selection == True:
            print("You can travel: (N)orth or (S)outh.")
        valid_selection = True
        choice = input("Direction: ")
        if choice.lower() == "n":
            y += 1
            #print(x, y)
        elif choice.lower() == "s":
            y -= 1
            #print(x,y)
        else:
            print("Not a valid direction!")
            valid_selection = False
    elif x == 3 and y == 1:
        print("Victory!")
        break
