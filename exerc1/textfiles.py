f = open("text.txt","r")
text = f.read()
f.close()
print(text)

with open("text.txt") as fobj:
    bio = fobj.read()
print(bio)

try:
    with open("secondtext.txt") as f:
        secondtext = f.read()
except FileNotFoundError:
    text = None

print(secondtext)