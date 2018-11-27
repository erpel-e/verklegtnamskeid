RANK = 0
COUNTRY = 1
RATING = 2
B_YEAR = 3


def read_file(file):
	def create_player_values():
		value_list = [None] * 4
		value_list[RANK] = int(rank)
		value_list[COUNTRY] = country
		value_list[RATING] = int(rating)
		value_list[B_YEAR] = int(b_year)
		return value_list

	player_dict = {}
	try:
		file_p = open(file, "r")
		for line in file_p:
			rank, name, country, rating, b_year = line.split(";")
			lastname, firstname = name.split(",")
			firstname = firstname.strip()
			lastname = lastname.strip()
			country = country.strip()
			dict_key = "{} {}".format(firstname, lastname)
			values = create_player_values()
			player_dict[dict_key] = values
		file_p.close

	except FileNotFoundError:
		print("File not found.")
	# print(player_dict)
	return player_dict


def header_print(header):
	print(header)
	print("-" * len(header))


def get_average_rating(p_dict, keys):
	player_ratings = [p_dict[player][RATING] for player in keys]
	return sum(player_ratings) / len(player_ratings)


def create_country_dict(p_dict):
	country_dict = {}
	for p_tuple in p_dict.items():
		player = p_tuple[0]
		values = p_tuple[1]
		country = values[COUNTRY]
		if country in country_dict:
			country_dict[country].append(player)
		else:
			player_list = [player]
			country_dict[country] = player_list
	return country_dict

def create_dict(p_dict, att_key):
	new_dict = {}
	for p_tuple in p_dict.items():
		player = p_tuple[0]
		values = p_tuple[1]
		key = values[att_key]
		if key in new_dict:
			new_dict[key].append(player)
		else:
			new_dict[key] = [player]
	#print(new_dict)
	return new_dict


def print_sorted(c_dict, p_dict):
	sorted_c_dict = sorted(c_dict.items())
	for country, player in sorted_c_dict:
		average_rating = get_average_rating(p_dict, player)
		print("{} ({}) ({:.1f}):".format(country, len(player), average_rating))
		for playe in player:
			ratings = p_dict[playe][RATING]
			print("{:>40} {:>10d}".format(playe, ratings))


# filename = input("Enter filename: ")

filename = "top_chess.csv"
p_dict = read_file(filename)
header = "Players by country:"
header2 = "Players by birth year:"
header_print(header)
#c_dict = create_country_dict(p_dict, COUNTRY)
c_dict = create_dict(p_dict, COUNTRY)
print_sorted(c_dict, p_dict)
#birth_year_dict(p_dict)
#b_dict = create_country_dict(p_dict, B_YEAR)
header_print(header2)
b_dict = create_dict(p_dict,B_YEAR)
print_sorted(b_dict, p_dict)