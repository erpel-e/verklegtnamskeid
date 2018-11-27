def input_vector(s):
    num = 1
    new_list = []
    for i in range(0,s):
        input_vector_1 = input("Element no"+ " "+ str(num)+": ")
        new_list.append(input_vector_1)
        num += 1
    return new_list

def dot_product(v1,v2):
    a_list = []
    for i in range (0,size):
        dot_prod = float(v1[1]+ float(v2[i]))
        a_list.append(dot_prod)
    summ = 0
    for i in a_list:
        summ += i
    return summ



# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))