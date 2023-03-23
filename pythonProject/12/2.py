import requests

kaupunki = input("Syötä paikkakunnan nimi: ")

api_avain = "dc5530198388ee7b2627e0660e902391"

url = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_avain}"
response = requests.get(url)

data = response.json()

lämpötila = round(data["main"]["temp"] - 273.15, 1)
säätila = data["weather"][0]["description"]
print(f"Säätila paikkakunnalla {kaupunki}: {säätila}. Lämpötila: {lämpötila} °C.")
