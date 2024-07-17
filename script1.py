name = input("Whats your name?").strip().title() 

# split string on chunk-variable
first, last = name.split(" ")

print(f"hi {first} - {last}")