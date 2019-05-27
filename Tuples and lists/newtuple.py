import sys
import timeit

list_test = timeit.timeit(stmt ="[1,2,3,4,5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

print("List time: ",list_test)
print("Tuple time: ",tuple_test)
#print(dir(sys))
#print(help(sys.getsizeof))

list_eg = [1, 2, 3, 4, 5]
tuple_eg = (1, 2, 3, 4, 5)

print("list size is: ", sys.getsizeof(list_eg))
print("size of tuple is: ", sys.getsizeof(tuple_eg))

empty_tuple = ()
test1 = ("a",)
test2 = ("a","b")
test3 = ("a","b","c")
print(empty_tuple)
print(test1)
print(test2)
print(test3)

survey = (25, "iceland",True)
age, country, knows_python = survey
print(survey)

""" 
a,b,c = 1,2,3,4
x,y,z = (1,2)
print(a,b,c)
print(x,y,z)
this will produce a ValueError in both cases
because in the first case is expecting to have 
three values and is getting four
in the second case is expecting
to have three values and is getting two.
"""