import re 

name = input("Whats your name? ").strip()
if matches := re.search(r"^(.+), (.+)$", name):
    finStr = matches.group(1) +" "+ matches.group(1)
print(f"hi, {finStr}")

# cut off comma 
# $> dava, david