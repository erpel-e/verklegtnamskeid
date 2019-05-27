my_file = open("words.txt")


def make_sentence(words):
	for word in words:
		word = word.strip()
		print(word, end=" ")
		if word == "":
			print("")


make_sentence(my_file)