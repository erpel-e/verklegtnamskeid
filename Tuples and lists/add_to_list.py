# Your functions should appear here
def populate_list(p_list):
    while True:
        element = input("Enter value to be added to list: ")
        if element.lower() == "exit":
            break
        p_list.append(element)
    return p_list

def triple_list(a_list):
    triple = a_list  * 3 
    return triple


# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)