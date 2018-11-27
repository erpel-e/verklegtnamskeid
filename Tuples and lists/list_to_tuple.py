def list_to_tuple(a_list):
    try:
        list_b = [int(i) for i in a_list]
        tuple_b = tuple(list_b)
        return tuple_b
    except:
        print("Error. Please enter only integers.")
        return ()
    


# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)