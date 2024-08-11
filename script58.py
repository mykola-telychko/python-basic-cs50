import csv 

players = []

with open("file.csv") as file: 
    reader = csv.reader(file)
    for city, country in reader: 
        players.append({"city": city, "country": country})


for player in sorted(players, key=lambda player: player["city"]): 
    print(f"{player['city']} is from {player['country']}")