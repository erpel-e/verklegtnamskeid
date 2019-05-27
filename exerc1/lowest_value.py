value1 = int(input("enter first value: "))
value2 = int(input("enter second value: "))
value3 = int(input("enter third value: "))

if value1 < value2 or value1 < value3:
    print(value1)
elif value2 < value1 or value2 < value3:
    print(value2)
elif value3 < value1 or value3 < value2:
    print(value3)