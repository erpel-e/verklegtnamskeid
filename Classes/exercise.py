class Player():
    def __init__(self,name,b_year,rating):
        self.name = name
        self.b_year = b_year
        self.rating = rating
        
    def __str__(self):
        return "\nName: {}\nYear:{}\nRating:{}".format(self.name, self.b_year,self.rating)


def get_highest_rated_player(players):
    highest_rated = Player("",0,0)
    for player in players:
        if player.rating > highest_rated.rating:
            highest_rated = player
    return player

def get_average_rating(players):
    n = len(players)
    s = float(sum([x.rating for x in players]))
    return "{:.1f}".format(s/n)


def main():
    number_of_players = int(input("Number of players: "))
    players = []
    print("-----Reading players-----")
    for i in range(number_of_players):
        name = input("Enter name: ")
        b_year = input("Enter birth year: ")
        rating = int(input("Enter rating: ")) 
        players.append(Player(name, b_year,rating))

    print("-----Displyaing players-----")
    for i in players:
        print(i)
        print()
    highest_rated = get_highest_rated_player(players)
    print("The highest rated player is:",highest_rated)
    average_rating = get_average_rating(players)
    print("The average rating is:\n",average_rating)

main()