import random

num = random.randint(1, 10)
veikkaus = None

while veikkaus != num:
    veikkaus = input("Kokeile arvata numero 1-10: ")
    veikkaus = int(veikkaus)

    if veikkaus == num:
        print("Oikein meni!")
        break
    elif veikkaus < num:
        print("Liian pieni arvaus, kokeile uudestaan")
    else:
        veikkaus > num
        print("Liian suuri arvaus, kokeile uudestaan")