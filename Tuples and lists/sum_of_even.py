def get_list():
    a_list = input(
        "Enter elements of list separated by commas: ").strip().split(',')
    return a_list


def even_sum(a_list):
    sum = 0
    list_b = [int(i) for i in a_list]
    b_list = [x for x in list_b if x%2 == 0]
    for x in b_list:
        sum += x

    return sum



# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
