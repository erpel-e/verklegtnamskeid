lis = ["", "5", "2", "4", "2", "", "9", "9", ""]


# dupl = [4, 7]
# for i in range(len(dupl)):
#     val = dupl[i]
#     for j in range(len(lis)):
#         if lis[j] == lis[val]:
#             print(lis[j])

not_dupl = []
dupl = []

for i in lis:
    print(i)
    if i not in not_dupl or i =='':
        not_dupl.append(i)
    else:
        dupl.append(i)
print(not_dupl)
print(dupl)