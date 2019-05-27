month = input()
day = int(input())

months = "january, february, mars, april, may, june, july, august, september, october, november, december"
holiday_1 = "New years's day"
holiday_2 = "National holiday"
holiday_3 = "Christmas day"

if month in months:
    if month == "january" and day == 1:
        print("Month:", month.capitalize() +
              "\nDay: {}".format(day), "{}".format(holiday_1))
    elif month == "june" and day == 17:
        print("Month:", month.capitalize() +
              "\nDay: {}".format(day), "{}".format(holiday_2))
    elif month == "december" and day == 25:
        print("Month:", month.capitalize() +
              "\nDay: {}".format(day), "{}".format(holiday_3))
    else:
        print("Month:", month.capitalize() +
              "\nDay: {}".format(day), "\nNot a holiday")