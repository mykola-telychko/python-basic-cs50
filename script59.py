import csv 

name = input("Whats your name? ")
home = input("Whats your home? ")

with open("file2.csv", "a") as file: 

    # old 
    # writer = csv.writer(file)
    # writer.writerow([name, home])
    
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})