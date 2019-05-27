my_file = open("words.txt")

def find_longest_word(words):
    longest_word = ""
    length = 0
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word.strip()
            length = len(longest_word)

    print("Longest word is " + "\'"+ longest_word +"\'" + " of length " + str(length))

find_longest_word(my_file)