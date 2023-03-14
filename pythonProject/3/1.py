pituus=int(input("Anna kuhan pituus: "))
if pituus < 37:
    print("Palauta järveen")
    vaje = 37-pituus
    print("Kuha on liian lyhyt",vaje, "senttimetrillä")
else: print("Kuha on tarpeeksi suuri")