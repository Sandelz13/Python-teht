# iteroiva while-looppi
# times = int(input("Montako kierrosta ajetaan?"))
times = 5
number = 1
while number <= times:
    #number += 1
    print(f"tulostetaan jotain, kierros: {number}")
    number = number + 1
    print(f"tulotetaan vaikka arvo olisi jo {number}")
print("silmukan suoritus loppui")
print(f"number-muuttujan arvo lopuksi: {number}")

# käyttäjästä riippuva toisto ja sisäkkäinen if-else
application_running = True
while application_running:
    command = input("Anna komento:")
    if command == 'lopeta':
        application_running = False
    elif command == "kerro vitsi":
        print("Chuck Norris...")
    elif command == "noppa":
        # Noppaesimerkki materiaalista (modattu)
        import random
        noppa1 = 0
        noppa2 = 0
        heitot = 0
        tuli_samat = False
        while tuli_samat == False:
            noppa1 = random.randint(1, 6)
            noppa2 = random.randint(1, 6)
            if noppa1 == noppa2 == 6:
                tuli_samat = True
            heitot = heitot + 1
            print(f"{heitot}. kierrokset tulokset: {noppa1}, {noppa2}")
        print(f"Tarvittiin {heitot} heittoa.")
    else:
        print("ok, jatketaan sitten")
    print("jatketaan suoritusta")
print("ohjelman suoritus loppuu")