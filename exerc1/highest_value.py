value1 = int(input("enter first value: "))
value2 = int(input("enter second value: "))

if value1 > value2 :
    print("{0} is bigger than {1} ".format(value1,value2))
elif value2 > value1 :
    print("{0} is bigger than {1} ".format(value2,value1))
else:
    print("values are equal")