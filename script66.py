import re 

name = input("Whats your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
# matches = re.search(r"^(.+), ?(.+)$", name) // for >dava,david
# matches = re.search(r"^(.+), *(.+)$", name) // for >dava,david

if matches: 
    name = matches.group(1) +" "+ matches.group(1)
print(f"hi, {name}")

# cut off comma 
# $> dava, david