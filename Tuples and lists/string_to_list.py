import string
# The main program starts here - DO NOT change it

def to_list(strings):
    if " " in strings:
        return strings.split()
    elif "," in strings:
        return strings.split(",")
    else: 
        return [strings]


the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)