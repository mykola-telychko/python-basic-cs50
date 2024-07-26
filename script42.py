import json
import requests 
import sys

# python .\script42.py weezer
if len(sys.argv) != 2:
    sys.exit()

respose = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

obj = respose.json()

for result in obj["results"]: 
    print(result["trackName"])

# print(respose.json())

# print(json.dumps(respose.json(), indent=2))