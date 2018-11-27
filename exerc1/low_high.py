low = int(input("enter a low value: "))
high = int(input("enter a high value: "))

""" i = 0
for i in range(low, high+1):
    print(i) """

""" turns = 0
a = 0

while a > 0:
    turns = int(input("enter how many times: "))
    for a in range(turns):
        a = int(input())
        if a % 2 == 0:
            print("you picked value {}".format(a))
        else:
            print("your pick is not odd number")
            break """
summ = 0
for x in range(low, high+1):
    summ += x
    print(summ)
