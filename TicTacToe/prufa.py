def myfirstfunction(counter, list):
	for i in list:
		for j in i:
			counter += 1
	return counter


mycounter = 0
mylist = ["whatever"]
count = myfirstfunction(mycounter, mylist)
print("Number of letters are:", count)
