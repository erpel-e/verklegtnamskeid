import string


def read_file(filename):
	with open(filename, "r") as f:
		content = f.read().split("<NEW DOCUMENT>")[1:]
	content = list(enumerate(content, 0))
	return content


def search_doc(content):
	target = input("Enter search words: ").lower().split()
	key_list = []
	for x in target:
		key_list.append(x)
	my_dict = {}
	t = [x[1].replace("\n", " ").strip(string.punctuation).lower() for x in content]
	for i in range(len(t)):
		for x in t[i].split():
			# for x in t[i].replace("-","").replace(",","").replace(".","").strip(string.punctuation).split():
			if x.strip(string.punctuation).lower() in my_dict:
				# if x.replace(",", "").strip(string.punctuation).lower() in my_dict:
				my_dict[x].add(i)
			else:
				my_dict[x] = set([i])
	sets = []
	for i in key_list:
		if i in my_dict.keys():
			sets.append(my_dict[i])
		else:
			sets.append([])
	# print(sets)
	if len(sets) > 0:
		result = " ".join([str(x) for x in list(set.intersection(*sets))])
		if len(result) == 0:
			print("No match.")
		else:
			print("Documents that fit search:", result, "\n")
	else:
		print("No match.")
	return None


def print_doc(content):
	doc = int(input("Enter document number: "))
	result = content[doc][1].strip()
	print("Document #{}".format(doc))
	print(result, "\n")
	return result


file = input("Document collection: ")
# file = "ap_docs.txt"
# p_list = read_file(file)
# search_doc(p_list)
quit = False

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
		print("Documents not found.")
		quit = True
