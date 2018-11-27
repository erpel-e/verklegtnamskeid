def get_word_list(file):
	file2 =	file.readlines()
	list1 = []
	for i in file2:
		list1.append(i.replace("\n","").replace(".","").split())
	list2 = []
	for i in list1:
		for j in i:
			list2.append(j.replace(",","").lower())
	print(list2)
	return list2
def word_list_to_counts(wordlist):
	d = {}
	for word in wordlist:
		if word in d:
			d[word] += 1
		else:
			d[word] = 1
	print(d)
	return d
def dict_to_tuple(dict):
	list1 = []
	for key, value in dict.items():
		list1.append((key, value))
	return list1
def main():
	filename = "file.txt"
	fpointer = open(filename)
	# Get a list of words from the file
	word_list = get_word_list(fpointer)
	# Transform the list to a dictionary of word-count pairs
	word_count_dict = word_list_to_counts(word_list)
	# Finally, makes a list of tuples from the dictionary
	word_count_tuples = dict_to_tuple(word_count_dict)
	print(sorted(word_count_tuples))


main()
