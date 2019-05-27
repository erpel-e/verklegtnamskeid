import string

sentence = input("Input a sentence: ")
unique_letters = []
bad_chars = string.whitespace + string.punctuation

for letter in sentence:
    if letter not in unique_letters:
        unique_letters += letter
for punc in string.punctuation:
    if punc in unique_letters:
        unique_letters.remove(punc)
for space in string.whitespace:
    if space in unique_letters:
        unique_letters.remove(space)        


print("Unique letters:", unique_letters)
