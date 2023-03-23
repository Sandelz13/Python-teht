import requests
import json

vitsi = requests.get("https://api.chucknorris.io/jokes/random")

vastaus = json.loads(vitsi.text)

print(vastaus["value"])


