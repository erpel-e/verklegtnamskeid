vowels = "aeiou"
i = 0
extension = "ay"
while True:
	word = input("Enter a word: ")
	first = word[0]
	new_word = ""
	if first in vowels:
		new_word = word + "yay"
		print(new_word)
	elif word == " ":
		new_word = " "
		print(new_word)
	elif word == ".":
		break
	else:
		for i in range(len(word)):
			if word[i] in vowels:
				new_word = word[i:] + word[:i] + extension
				print(new_word)
				break
		else:
			print(word)


