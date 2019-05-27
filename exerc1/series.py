initial = int(input("Initial value: "))
step = int(input("Step: "))

#i = 0
summ = 0
while summ < 100:
    summ = initial + summ
    print(initial, end=" ")
    initial+= step
print("\nSum of series is: ",summ)
""" j = 0
summa = 0
while initial >= 0:
    summa = summ
    if summa >=100:
        break 
    while initial >= 0:
        summ = summ + initial
        print(initial, end=" ")
        initial += step
        if summ >= 100:
            break
print("\nSum of series: ", summa) """

