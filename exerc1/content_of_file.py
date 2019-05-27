input_file = open("test.txt")

for word in input_file:
    word = word.replace(" ","")
    word = word.strip()
    print(word, end="")

