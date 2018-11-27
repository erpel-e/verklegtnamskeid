word = list("hasdfahsdklf")
#word = word.split()
word.sort()
print(word)
new_word = "hello darkness my old friend".split()
new_word.sort()
print(new_word)

my_str = "this is something"

string_elements = my_str.split()
reversed_elements = []
for e in string_elements:
    reversed_elements.append(e[::-1])
print(reversed_elements)
reversed_elements_joined = " ".join(reversed_elements)
print(reversed_elements_joined)