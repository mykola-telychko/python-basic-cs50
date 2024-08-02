players = []; 

with open("file.csv") as file: 
    for line in file: 
        city, country = line.rstrip().split(",")
        
        player = {}
        player["city"] = city
        player["country"] = country

        players.append(player)

for player in players: 
    print(f"{player['city']} is in {player['country']}")