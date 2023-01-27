import random

def throw_dice(dice_sides):
    return random.randint(1, dice_sides)

dice_sides = int(input("Anna nopan tahkojen määrä: "))
max_value = dice_sides

while True:
    number_on_dice = throw_dice(dice_sides)
    print("Silmäluku:", number_on_dice)
    if number == max_value:
        break
