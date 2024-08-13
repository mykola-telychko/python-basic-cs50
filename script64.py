name = input("Whats your name? ").strip()

if "," in name: 
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hi, {name}");