import random
import string


def get_word_string(file):
	try:
		wordString = ''
		with open(file,"r") as f:
			for line in f:
				wordString += line
	except:
		print("File {} not found".format(file))

	return wordString
def scramble_word(word):
	j = word.strip(string.punctuation)
	l = list(j)
	l = list(j[1:len(j)-1])
	random.shuffle(l)

	scrambled_word = ''
	if word[len(word)-1] in string.punctuation:
		scrambled_word = word[0] + ''.join(l) + j[len(j)-1] + word[len(word)-1]
	else:
		scrambled_word = word[0] + ''.join(l) + word[len(word)-1]

	return scrambled_word

def scramble_string(s):
	new_words = []
	s = s.replace('\n', ' ')
	words = s.split(' ')
	for word in words:
		if len(word) < 4:
			new_words.append(word)
		else:
			new_words.append(scramble_word(word))
	return ' '.join(new_words)

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)
