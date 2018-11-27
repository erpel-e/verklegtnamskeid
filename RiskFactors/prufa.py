def get_file(file):
	try:
		rest_l = []
		list_a = []
		with open(file, "r") as f:
			first_line = f.readline()
			rest = f.readlines()[1:]
		for i in rest:
			rest_l.append(i)
		for i in first_line.split(","):
			list_a.append(i)
			#print(rest_l, list_a)
			return list_a
	except:
		print("File {} not found".format(file))

filename = input("Enter name of file: ")
print(get_file(filename))


listi[0][1]













"""
brands = [["Microsoft", "120", "38", "11"], ["Apple", "150", "40", "18"], ["Google", "110", "35", "14"]]
list2 = ['10.79', '11.9', '12.06', '12.24', '12.37', '12.39', '12.41', '13.06', '13.11', '13.69', '13.8', '14.01',
         '14.62', '14.66', '15.71', '16.13', '17.96', '18.28', '18.34', '19.56', '19.6', '20.02', '20.25', '21.64',
         '22.67', '23.71', '24.62', '4.84', '5.07', '5.92', '6.34', '6.7', '7.06', '7.38', '7.88', '7.99', '8.3',
         '8.34', '8.42', '8.74', '8.76', '8.85', '9.16', '9.19', '9.25', '9.6', '9.6', '9.85', '9.92', '9.96']
print(sorted(list2))
print(min(brand[1] for brand in brands))
company = None
minwage = None

for brand in brands:
	if minwage is None or brand[1] < minwage:
		minwage = brand[1]
		company = brand[0]

print('Lowest wage was: %s,%s' % (minwage, company))

sorted_brands = sorted(brands, key=lambda x: int(x[1]))

print(
	'The lowest wage: {}, {}, the highest wage: {}, {}'.format(sorted_brands[0][0], sorted_brands[0][1],
	                                                           sorted_brands[-1][0], sorted_brands[-1][1]))
print(
	'The lowest working hours: {}, {}, the highest working hours: {}, {}'.format(sorted_brands[0][0],
	                                                                             sorted_brands[0][2],
	                                                                             sorted_brands[-1][0],
	                                                                             sorted_brands[-1][2]))
print(
	'The lowest asga: {}, {}, the highest asdfa: {}, {}'.format(sorted_brands[0][0], sorted_brands[0][3],
	                                                         sorted_brands[-1][0], sorted_brands[-1][3]))
wage = []
for var in range(len(brands)):
	wage.append(brands[var][1])

min = wage.index(min(wage))
print("The highest wage :{0}, {1}".format(brands[min][0], brands[min][1]))
with open('strings.txt', 'w') as f:
	for item in collect_first:
		f.write("%s\n" % item)
"""