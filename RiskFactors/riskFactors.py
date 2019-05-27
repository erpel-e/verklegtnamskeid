def get_file(file):
	list_a = []
	with open(file, "r") as f:
		first_line = f.readline()
		rest = f.readlines()[1:]
		for i in first_line.split(","):
			list_a.append(i)
	return list_a, rest

def read_file(list1, rest):
	list3 = []
	collect_first = []
	heart_d = []
	motor_d = []
	teen_b = []
	adult_s = []
	adult_ob = []

	for a in rest:
		list3.append(a.replace("\n", "").replace("%", "").split(","))
	#print(list3)

	for x in list3:
		collect_first.append([x[0], float(x[1]), float(x[5]), float(x[7]), float(x[11]), float(x[13])])
	#print(collect_first)
	for var in range(len(collect_first)):
		heart_d.append(collect_first[var][1])
	minn = heart_d.index(min(heart_d, key=float))
	maxx = heart_d.index((max(heart_d, key=float)))

	for var in range(len(collect_first)):
		motor_d.append(collect_first[var][2])
	min_m = motor_d.index(min(motor_d, key=float))
	max_m = motor_d.index((max(motor_d, key=float)))

	for var in range(len(collect_first)):
		teen_b.append(collect_first[var][3])
	min_t = teen_b.index(min(teen_b, key=float))
	max_t = teen_b.index((max(teen_b, key=float)))

	for var in range(len(collect_first)):
		adult_s.append(collect_first[var][4])
	min_as = adult_s.index(min(adult_s, key=float))
	max_as = adult_s.index((max(adult_s, key=float)))

	for var in range(len(collect_first)):
		adult_ob.append(collect_first[var][5])
	min_ob = adult_ob.index(min(adult_ob, key=float))
	max_ob = adult_ob.index((max(adult_ob, key=float)))

	print("{:<33}{:<21}{:>6.1f}{}{:<15}{:>6.1f}".format(list1[1] + ":", collect_first[minn][0], collect_first[minn][1],
	                                              "      ",
	                                              collect_first[maxx][0], collect_first[maxx][1]))
	print("{:<33}{:<21}{:>6.1f}{}{:<15}{:>6.1f}".format(list1[5] + ":", collect_first[min_m][0], collect_first[min_m][2],
	                                              "      ",
	                                              collect_first[max_m][0], collect_first[max_m][2]))
	print("{:<33}{:<21}{:>6.1f}{}{:<15}{:>6.1f}".format(list1[7] + ":", collect_first[min_t][0], collect_first[min_t][3],
	                                              "      ",
	                                              collect_first[max_t][0], collect_first[max_t][3]))
	print("{:<33}{:<21}{:>6.1f}{}{:<15}{:>6.1f}".format(list1[11] + ":", collect_first[min_as][0], collect_first[min_as][4],
	                                              "      ", collect_first[max_as][0], collect_first[max_as][4]))
	print("{:<33}{:<21}{:>6.1f}{}{:<15}{:>6.1f}".format(list1[13] + ":", collect_first[min_ob][0], collect_first[min_ob][5],
	                                              "      ", collect_first[max_ob][0], collect_first[max_ob][5]))


def header():
	print("{:<33}{:<21}{:>6}{}{:<15}{:>6}".format("Indicator", "Min", "", "      ", "Max", ""))
	print("-" * 87)

#--------------Main Program---------------#
try:
	filename = input("Enter filename containing csv data: ")
	list1, rest_l = get_file(filename)
	header()
	read_file = read_file(list1, rest_l)
except:
	print("Cannot find file {}".format(filename))
	header()
