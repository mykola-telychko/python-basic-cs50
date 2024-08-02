players = []; 

with open("file.csv") as file: 
    for line in file: 
        city, country = line.rstrip().split(",")
        #  same sh like script54     
        player = {"city": city, "country": country }
        players.append(player)

for player in sorted(players, key=lambda player: player['city']): 
    print(f"{player['city']} is in {player['country']}")

