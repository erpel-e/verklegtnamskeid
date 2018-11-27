def fibo(integer):
    n1 = 1
    n2 = 1
    count = 0

    if integer <= 0:
        print("Please enter a positive integer")
    elif integer == 1:
        #print(integer,":")
        print()
    else:
        #print(integer)
        while count < integer:
            print(n1,end=' ')
            nth = n1 + n2
       # update values
            n1 = n2
            n2 = nth
            count += 1
n = int(input("Input the length of Fibonacci sequence (n>=1): "))
fibo(n)