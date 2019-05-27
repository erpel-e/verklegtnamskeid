position = int(input("Input a position between 1 and 10: "))

i = 1
while i>0:
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    choice = input("Input your choice: ")
    if choice == "r":
        position +=1
        print("New position is: ",position)
        #choice = input("Input your choice: ")
    elif choice == "l":
        position -=1
        print("New position is: ",position)
        #choice = input("Input your choice: ")
    else: 
        break