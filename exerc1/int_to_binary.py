my_int = int(input('Give me an int >= 0: '))
original_int = str(my_int)
empty = ""
if my_int == 0:
    empty = "0"
else:

    for i in range(my_int):
        bin_div = my_int %2
        if my_int / 2 != 0:
            my_int= my_int // 2
            empty = empty + str(bin_div)


# Fill in the missing code
print("The binary of", original_int, "is", empty[::-1])