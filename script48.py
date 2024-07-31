name = input("Whats your name? ")

# write
file = open("name.txt", "w")

# append
# file = open("name.txt", "a")

# file.write(name)
file.write(f"{name}\n")

file.close()