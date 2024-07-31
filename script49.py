name = input("Whats you name? ")

with open("names.txt", "a") as file: 
    file.write(f"{name}\n") 