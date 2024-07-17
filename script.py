# ask user for their name 
name = input("Whats your name? "); 

# try separator
# print("hello, ", name, sep="???");

# eval variable 
# print(f"hi, {name}");

# Remove whitespace (like trim)
# name = name.strip().capitalize();
name = name.strip().title(); # apply to every next word

print(f"hi, {name}");


