def menu_selection():
	print("Menu:")
	inp = input("add(a), remove(r), find(f): ")
	return inp
def execute_selection(choice, a_dict):
	if choice == "a":
		key = input("Key: ")
		value = input("Value: ")
		add_to_dict(a_dict, key, value)
	elif choice == "r":
		key = input("key to remove: ")
		remove_from_dict(a_dict, key)
	elif choice == "f":
		key = input("Key to locate: ")
		find_key(a_dict, key)
	else:
		print("Invalid choice.")
def dict_to_tuples(dict):
	list1 = []
	for key, value in dict.items():
		list1.append((key, value))
	return list1
def add_to_dict(dict, key, value):
	if key in dict:
		print("Error. Key already exists.")
	else:
		dict[key] = value
	return dict
def remove_from_dict(r_dict, key):
	if key in r_dict:
		return r_dict.pop(key)
	else:
		print("No such key exists in the dictionary.")

def find_key(f_dict, key):
	if key in f_dict:
		value = f_dict[key]
		print("Value:",value)
	else:
		print("Key not found.")
# Do not change this main function
def main():
	more = True
	a_dict = {}
	while more:
		choice = menu_selection()
		execute_selection(choice, a_dict)
		again = input("More (y/n)? ")
		more = again.lower() == 'y'
	dictlist = dict_to_tuples(a_dict)
	print(sorted(dictlist))


main()
