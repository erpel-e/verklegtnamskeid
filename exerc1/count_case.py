# Your function definition goes here
def count_case(user):
    upper = 0
    lower = 0
    for letter in user_input:
        if letter.isupper() :
            upper +=1
        elif letter.islower():
            lower += 1
    return upper, lower

user_input = input("Enter a string: ")

upper,lower = count_case(user_input)

# Call the function here

print("Upper case count: ", upper)
print("Lower case count: ", lower)