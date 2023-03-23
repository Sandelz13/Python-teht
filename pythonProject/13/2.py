import requests
import json

# Hae satunnainen Chuck Norris -vitsi rajapinnasta
response = requests.get("https://api.chucknorris.io/jokes/random")

# Muunna vastauksen JSON-muotoiseksi
data = json.loads(response.text)

# Tulosta vitsin teksti
print(data["value"])