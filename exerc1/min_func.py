def min_number():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    if first < second:
        return first
    else:
        return second
    print()


minimum = min_number()
# Call the function here
print("Minimum: ",minimum)
