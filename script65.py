import re 

name = input("Whats your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)

if matches: 
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"hi, {name}")

# cut off comma 
# $> dava, david