players = [{
            "Ivanchuk": "UA",
            "Tal": "Latvia", 
            "Fisher": "USA",
}]

# dict in list 
players2 = [
    { "name": "Ivanchuk", "country": "UA", "grade": "GM" },
    { "name": "Tal", "country": "Latvia", "grade": "GM" },
    { "name": "Fisher", "country": "USA", "grade": "FM" },
]

for person in players2: 
    print(person["name"], person["country"], person["grade"]  )