names = set()

while True:
    name = input("Syötä nimi: ")

    if name == "":
        break

    if name in names:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        names.add(name)

print("Syötetyt nimet:")
for name in names:
    print(name)