def dictionary(p_d):
	name = input("Name: ")
	number = input("Number: ")
	p_d[name] = number
	return p_d


def sort_d(dict):
	list1 = []
	for key, value in dict.items():
		list1.append((key, value))
	return list1


def d_t_l(dd):
	return [(key, value) for key, value in dd.items()]


d = {}
more = True
while more:
	dictionary(d)
	check = input("More data (y/n)? ")
	if check.lower() == "y":
		pass
	elif check.lower() == "n":
		print(sorted(sort_d(d)))
		more = False
