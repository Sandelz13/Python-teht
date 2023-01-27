def from_gal_to_litre(gallons):
        return gallons * 3.785

while True:
    gallons = float(input("Anna bensan määrä gallonoina. Negatiivinen syöte lopettaa: "))
    if gallons < 0:
        break
    litres = from_gal_to_litre(gallons)
    print("Bensan määrä litroina: ", litres)