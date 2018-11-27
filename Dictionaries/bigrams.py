import string
def read_file(file):
	list2 = []
	with open(file, "r") as f:
		for i in f:
			for word in i.split():
				list2.append(word.strip(string.punctuation).replace("\n", "").replace(".", "").lower())
	return list2


def bigrams(a_list):
	bigrams = [(a_list[i], a_list[i + 1]) for i in range(len(a_list)-1)]
	mydict = {}
	for i in bigrams:
		if i in mydict:
			mydict[i] += 1
		else:
			mydict[i] = 1
	list3 = []
	for key, value in mydict.items():
		list3.append((key, value))
	list3.sort(key=lambda tuple: tuple[1], reverse=True)
	#print(list3[:10])
	return list3[:10]


file = input("Enter name of file: ")

#read_file("bigram.txt")
read_file(file)
bigr = bigrams(read_file(file))
print(bigr)