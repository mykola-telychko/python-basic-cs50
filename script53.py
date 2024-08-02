players = []; 

with open("file.csv") as file: 
    for line in file: 
        name, house = line.rstrip().split(",")
        players.append(f"{name} is in {house}")

for player in sorted(players): 
    print(player)