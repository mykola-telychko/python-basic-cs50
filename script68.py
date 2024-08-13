url = input("URL: ").strip()

# username = url.replace("https://x.com/", "")
username = url.removeprefix("https://x.com/")

print(f"Username: {username}")

# > https://x.com/elonmusk