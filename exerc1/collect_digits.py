s = input("Input a string: ")

empty = " "

for letter in s:
    if (letter.isdigit()):
        empty = empty + letter
print(empty)
        