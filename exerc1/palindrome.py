import string
# palindrome function definition goes here
def palindrome_check(word):

    modified_str = word.lower()

    bad_chars = string.whitespace + string.punctuation

    for char in modified_str:
        if char in bad_chars:  # remove bad characters
            modified_str = modified_str.replace(char, '')
    if modified_str == modified_str[::-1]:  # i t i s a palindrome
        print("\"{}\" is a palindrome".format(word))
    else:
        print("\"{}\" is not a palindrome".format(word))

# call the function and print out the appropriate message
in_str = input("Enter a string: ")
palindrome_check(in_str)
