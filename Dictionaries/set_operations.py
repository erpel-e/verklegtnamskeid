def ret_set(list):
	a_set = set()
	for i in list:
		if i not in a_set:
			a_set.add(int(i))
	return a_set


def intersectionn(a_list, b_list):
	intersect = set(ret_set(a_list)).intersection(set(ret_set(b_list)))
	return intersect


def unionn(a_list, b_list):
	unio = set(ret_set(a_list)).union(set(ret_set(b_list)))
	return unio


def difference(a_list, b_list):
	diff = set(ret_set(a_list)).difference(set(ret_set(b_list)))
	return diff


list1 = input("Input a list of integers separated with a comma: ").split(",")
list2 = input("Input a list of integers separated with a comma: ").split(",")
print(ret_set(list1))
print(ret_set(list2))
quit = False
#print(difference(list1, list2))

while not quit:
	print("1. Intersection")
	print("2. Union")
	print("3. Difference")
	print("4. Quit")
	operation = int(input("Set operation: "))
	if operation == 1:
		print(intersectionn(list1, list2))
	elif operation == 2:
		print(unionn(list1, list2))
	elif operation == 3:
		print(difference(list1, list2))
	elif operation == 4:
		quit = True