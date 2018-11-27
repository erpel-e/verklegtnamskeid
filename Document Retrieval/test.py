import string


def read_file(filename):
	with open(filename, "r") as f:
		content = f.read().split("<NEW DOCUMENT>")[1:]
	content = list(enumerate(content, 0))
	return content


def search_doc(content):
	#target1 = "on"
	target = input("Enter search words: ").split()
	#target = target.strip()
	key_list = []
	for x in target:
		key_list.append(x)
	#print(key_list)
	my_dict = {}
	t = [x[1].replace("\n", "").strip().lower() for x in content]
	for i in range(len(t)):
		for x in t[i].split():
			if x.lower() in my_dict:
				my_dict[x].add(i)
			else:
				my_dict[x] = set([i])
	#print(my_dict)
	sets = []
	for i in key_list:
		if i in my_dict.keys():
			#print(my_dict[i])
			sets.append(my_dict[i])
	#print(sets)
	inter_set = set.intersection(*sets)
	for i in inter_set:
		print(i,end=" ")
	#print(inter_set)
	return None
"""	
	count = []
	pos = -1
	for i in b:
		for x in i:
			pos += 1
			x = x.replace(",", "").split()
			for a in x:
				if a.lower() == target1.lower():
					for y in x:
						if y.lower() == target2.lower():
							count.append(pos)
	result = " ".join([str(x) for x in list(set(count))])
	if len(count) > 0:
		print("Documents that fit search:", result, "\n")
	else:
		print("No match.\n", )
	return None


def print_doc(content):
	doc = int(input("Enter document number: "))
	result = content[doc][1].strip()
	print("Document #{}".format(doc))
	print(result, "\n")
	return result
"""


# file = input("Document collection: ")
file = "ap_docs.txt"
p_list = read_file(file)
search_doc(p_list)
quit = False

"""
while not quit:
	try:
		p_list = read_file(file)
		print("What would you like to do?")
		print("1. Search Documents")
		print("2. Print Document")
		print("3. Quit Program")
		choice = int(input("> "))
		if choice == 1:
			search_doc(p_list)
		elif choice == 2:
			print_doc(p_list)
		elif choice == 3:
			print("Exiting program.")
			quit = True
		else:
			quit = True
	except:
		print("Document not found.")
		quit = True



list_x = ["this is the first", "this is the second"]
my_dict = {}
for i in range(len(list_x)):
	for x in list_x[i].split():
		if x in my_dict:
			my_dict[x].add(i)
		else:
			my_dict[x] = set([i])

print(my_dict)
"""
