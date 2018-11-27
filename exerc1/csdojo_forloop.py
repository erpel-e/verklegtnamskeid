a = ["apple", "orange", "google"]
for a in a:
    print(a)

b = [20, 10, 5]
total = 0
for i in b:
    # print(b)
    total = total + i
print(total)

c = list(range(1, 5))
print(c)
total2 = 0
for i in range(1, 5):
    print(i)
    total2 += i
print(total2)


print(list(range(1, 8)))
total3 = 0
for i in range(1, 8):
    if i % 3 == 0:
        total3 += i
print(total3)

total4 = 0
#print(list(range(1, 100)))
for i in range(1, 100):
    if i % 3 == 0:
        total4 += i
    elif i % 5 == 0:
        total4 += i
print(total4)
