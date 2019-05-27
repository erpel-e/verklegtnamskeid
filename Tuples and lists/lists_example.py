x = [1,2,5]


def f(x):
    return x**2

l = [f(i) for i in x ]
print(l)

string = ["hello 1245 world"]

li = [y for y in string if y.isdigit()]
print(li)