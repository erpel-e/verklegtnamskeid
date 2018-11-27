# Main program starts here - DO NOT CHANGE
pascal = []
def make_new_row(row):
    k = len(row)
    if k == 0:
        help_list = [1]
        pascal.append(help_list)
        return help_list

    if k == 1:
        help_list = [1, 1]
        pascal.append(help_list)
        return help_list
    help_list = [l for l in range(k+1)]
    for y in range(1,k):
        help_list[0] = 1
        help_list[k] = 1
        help_list[y] = pascal[k-1][y]+ pascal[k-1][y-1]

    pascal.append(help_list)
    return help_list


height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)
