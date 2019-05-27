a = [3, 10, -1]
print(a)
a.append(1)
print(a)
a.append("hello")
print(a)
a.append([1,2])
print(a)
a.pop()
print(a)
a.pop()
print(a)
print(a[0])
print(a[3])
a[0] = 100
print(a)
b = ["bannana","apple", "microsoft"]
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)
b[0], b[2] = b[2],b[0]
print(b)