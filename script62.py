email = input("Whats your email? ").strip()

username, domain = email.split("@")

# if username and "." in domain:
if username and  domain.endswith(".edu"):

    print("Valid")
else: 
    print("Invalid")