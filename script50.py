with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines: 
    print("hi", line.rstrip())
    # print("hi", line)