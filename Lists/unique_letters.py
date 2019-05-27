import string

sentence = input("Input a sentence: ")

unique_letters = []
bad_chars = string.whitespace + string.punctuation
new_sentence = ""
for char in sentence:
	if char in bad_chars:
		new_sentence = new_sentence.replace(char, "")
		print(new_sentence)

print("Unique letters:", unique_letters)