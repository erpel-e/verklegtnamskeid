#removes the last digit of a number
number = "93,235"
cleanedNumber = ""
for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleanedNumber = number[i]

newNumber = int(cleanedNumber)

print("The cleaned number is {}".format(newNumber))