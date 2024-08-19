students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Luna", "house": "Ravenclaw"}
]

# old
# houses = []
# houses = list()
# for student in students: 
#     if student["house"] not in houses: 
#         houses.append(student["house"])

houses = set()

for student in students: 
    houses.add(student["house"])

for house in sorted(houses): 
    print(house)