def f(x):
    x += 1
    print("in f(x) : x = ", x)
    return x

x = 3
z = f(x)
def is_even_with_return(i):
    print("with return")
    remainder = i % 2
    return remainder == 0

is_even_with_return(3)
print(is_even_with_return(3))

def is_even_without_return(i):
    print("without return")
    remainder = i % 2

is_even_without_return(4)
print(is_even_without_return(4))

def is_even(i):
    remainder = i % 2
    return remainder == 0

for i in range(20):
    if is_even(i):
        print(i, "even")
    else:
        print(i,"odd")

def g(y):
    print(x)
    print(x+1)

x = 5
g(x)
print(x)
