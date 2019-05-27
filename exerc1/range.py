# The function definition goes here


def range(number):
    if number > 1 and number < 555:
        print(number, "is in range!")
    else:
        print(number, "is outside the range!")


num = int(input("Enter a number: "))
# You call the function here
range(num)
