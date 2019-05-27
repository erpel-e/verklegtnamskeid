dollar = 0
numerator = 0
denominator = 0
price = 0


def check_int(ch_shares):
	while True:
		try:
			ch_dollar, ch_numerator, ch_denominator = input("Enter price (dollars, numerator, denominator): ").split()
			ch_dollar = int(ch_dollar)
			ch_numerator = int(ch_numerator)
			ch_denominator = int(ch_denominator)
			what_price = ch_dollar + (ch_numerator / ch_denominator)
			total = ch_shares * what_price
			print(
				"{} shares with market price {} {}/{} have value ${:.2f}".format(ch_shares, ch_dollar, ch_numerator, ch_denominator,
			                                                                 total))
			return False
		except ValueError:
			print("Invalid price!")




while True:
	try:
		shares = int(input("Enter number of shares: "))
	except ValueError:
		print("Invalid number!")
		continue
	price = check_int(shares)
	to_continue = input("Continue: ")
	if to_continue.lower() == "y":
		continue
	elif to_continue.lower() == "n":
		break
