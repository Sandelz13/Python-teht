import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("Kokeile arvata numero 1-10: ")
    guess = int(guess)

    if guess == num:
        print("Oikein meni!")
        break
    elif guess < num:
        print("Liian pieni arvaus, kokeile uudestaan")
    else:
        guess > num
        print("Liian suuri arvaus, kokeile uudestaan")