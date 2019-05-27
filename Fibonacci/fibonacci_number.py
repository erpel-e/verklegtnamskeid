""" def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,11):
    print(n, ":", fibonacci(n)) 
    
This way of showing fibonacci number works but 
it is very slow because the computer has 
to do so many calculations each time that 
looks for a new number, so we are going to use
a different way
"""
""" fibonacci_cache = {}
def fibonacci(n):
    # if we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    # Cache the value and return it
    fibonacci_cache[n] = value
    return value
for n in range(1,101):
    print(n, ":",fibonacci(n))

The second way performs much better and quick but there
is still another way that performs even better.    
 """
from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(n):
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


""" for n in range(1,500):
    print(n, ":", fibonacci(n)) """

#fibonacci(fibonacci(2.1)) check to make sure the return of error works
# compute the ratio
for n in range(1, 51):
    print(fibonacci(n+1) / fibonacci(n))
