import string


def read_file(filename):
	with open(filename, "r") as f:
		content = f.read().split("<NEW DOCUMENT>")[1:]
	content = list(enumerate(content, 0))
	return content


def search_doc(content):
	l = [x[1].replace("\n", "").strip() for x in content]
	b = [[x] for x in l]
	#target1 = "stock"
	#target2 = "prices"
	target1, target2 = input("Enter search words: ").split()
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


file = input("Document collection: ")
#file = "ap_docs2.txt"
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
		print("Document not found.")
		quit = True
