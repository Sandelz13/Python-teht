airports = {}

while True:
    action = input("Haluatko lisätä(lisää) uuden lentoaseman, hakea(hae) lentoaseman tiedot vai lopettaa(lopeta): ")

    if action == "lisää":
        icao = input("Syötä lentoaseman ICAO-koodi: ")
        name = input("Syötä lentoaseman nimi: ")
        airports[icao] = name
    elif action == "hae":
        icao = input("Syötä haettavan lentoaseman ICAO-koodi: ")
        if icao in airports:
            print("Lentoasema:", airports[icao])
        else:
            print("Lentoasemaa ei löytynyt.")
    elif action == "lopeta":
        print("Ok, näkemiin!")
        break
    else:
        print("En ymmärrä, tarkista kirjoitusvirheet.")