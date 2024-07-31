with open("file.csv") as file:
    for line in file: 
        city, country = line.rstrip().split(",")
        print(f"{city} is in {country}")

# old
# row = line.rstrip().split(",")
# print(f"{row[0]} is in {row[1]}")
  