players = []; 

with open("file.csv") as file: 
    for line in file: 
        city, country = line.rstrip().split(",")
        #  same sh like script54     
        player = {"city": city, "country": country }
        players.append(player)

def get_name(lib):
    return lib["city"]


for player in sorted(players, key=get_name, reverse=True): 
    print(f"{player['city']} is in {player['country']}")


# for player in players: 
#     print(f"{player['city']} is in {player['country']}")