def fibo(length):
    fibonacci = list((1, 1))
    if length != 1:
        while len(fibonacci) < length: 
            temp_num = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(temp_num)
        print(*fibonacci, sep=" ")
    else:
        print("1")


n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here        
fibo(n)