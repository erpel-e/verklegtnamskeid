""" total = 0
for i in range(1, 5):
    total += i
print(total)

total2 = 0
j = 1
while j < 5:
    total2 += j
    j += 1
print(total2)

given_list = [5, 4, 3, 2, 1]
total3 = 0
i = 0
while i <len(given_list) and given_list[i] > 0:
    total3 += given_list[i]
    i += 1
print(total3)

given_list2 = [5, 4, 3, 2, 1,-1,-2,-4]
total4 = 0
for i in given_list2:
    if i <= 0:
        break
    total4 +=i
print(total4)

given_list3 = [5, 4, 3, 2, 1,-1,-2,-4]
total5 = 0
i = 0
while True:
    total5 += given_list3[i]
    i += 1
    if given_list3[i] <= 0:
        break
print(total5) """
given_list4 = [8,6, 5, 2, 1, -1]
total6 = 0
""" total7 = 0
i = 0
while i < (len(given_list4)):
    total6 += given_list4[i]
    i += 1
    j = total7
    while j < (len(given_list4)):
        total7 += given_list4[j]
        j += 1
        if given_list4[j] <= 0:
            break
print(total7)
print(total6)
print(total6-total7) """
""" for i in given_list4:
    if i < 0:
        total6 += i
print(total6) """
j = len(given_list4)-1
while given_list4[j]<0:
    total6 += given_list4[j]
    j -= 1
print(total6)