def get_list():
	a_list = input("Enter elements of list separated by commas: ").strip().split(',')
	return a_list


def get_integer(prompt):
	val = int(input(prompt))
	return val


def transform(list_1, list_2, index_1, index_2):
	new_list = []
	for i in range(len(list_1)):
		if i in range(index_1+1, index_2+1):
			new_list.append(i)
			#print(i)
	for i in reversed(new_list):
		list_2.append(str(i))

	for i in range(len(new_list)):
		del list_1[index_1]
	return list_1, list_2


#Main program starts here - DO NOT change it
#list1 = get_list()
#list2 = get_list()
#index1 = get_integer("Enter from value: ")
#index2 = get_integer("Enter to value: ")
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [100,200,300]
index1 = 4
index2 = 7


transform(list1, list2, index1, index2)
print(list1)
print(list2)
