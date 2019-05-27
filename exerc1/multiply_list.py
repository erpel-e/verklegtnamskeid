def list_multiply(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total

print(list_multiply((2,4,5)))