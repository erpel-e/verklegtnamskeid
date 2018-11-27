def common_letter(name, last):
	list1 = []
	common_letter = []
	for i in name:
		if i in last:
			list1.append(i)
	for i in list1:
		if i not in common_letter:
			common_letter.append(i)
	return common_letter


def set_common(a, b):
	set_name = set(a)
	set_last = set(b)
	intersection = set_name.intersection(set_last)
	list1 = []
	for i in intersection:
		list1.append(i)
	return list1

name, last = input("Enter name: ").lower().split()

a_list = common_letter(name, last)
print(sorted(a_list))
b_list = set_common(name, last)
print(sorted(b_list))
