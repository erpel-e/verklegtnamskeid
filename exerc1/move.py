LOWER = 1
HIGHER = 10


def move(positioning):
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")


position = int(input("Input a position between 1 and 10: "))

while True:
    move(position)
    choice = input("Input your choice: ")
    if choice == "r" and position < HIGHER:
        position += 1
        print("New position is:", position)
    elif choice == "r" and position == HIGHER:
        print("New position is:", position)
    elif choice == "l" and position > LOWER:
        position -= 1
        print("New position is:", position)
    elif choice == "l" and position == LOWER:
        print("New position is:", position)
    else:
        print("New position is:", position)
        break
