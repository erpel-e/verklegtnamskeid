x = 1
y = 1
LOW = 1
HIGH = 3
valid_selection = True

def choice_option(i,valid_selection):
    if i == "n":
        #print(i, "is a valid selection")
        return None
    elif i == "e":
        #print(i, "is a valid selection")
        return None
    elif i == "s":
        #print(i, "is a valid selection")
        return None
    elif i == "w":
        #print(i, "is a valid selection")
        return None
    else:
        print("Not a valid Direction!")
        valid_selection = False


def increment(choice, x,y):
    if choice == "e" and LOW <= x < HIGH:
        x += 1
    elif choice == "w" and LOW < x <= HIGH:
        x -= 1
    elif choice == "n" and LOW <= y < HIGH:
        y += 1
    elif choice == "s" and LOW < y <= HIGH:
        y -= 1    
    return x,y

def position(x,y):
    if x == 1 and y == 1:
        print("You can travel: (N)orth.")
    elif x == 1 and y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")

while True:
    if valid_selection == True:
        position(x,y)
    valid_selection = True
    something = input("Direction: ")
    x,y = increment(something, x,y)
    valid_selection = choice_option(something, valid_selection)
    #choice_option(something,valid_selection)
    print(x, y)
