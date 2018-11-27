def is_prime(prime):
    if prime > 1:
        for a in range(2, prime):
            if(prime % a) == 0:
                print(prime, "is not prime")
                break
        else:
            print(prime, "is a prime")
    else:
        print(prime, "is not a prime")


# is_prime function definition goes here

num = int(input("Input an integer greater than 1: "))
is_prime(num)

# Call the function here and print out the appropriate message
