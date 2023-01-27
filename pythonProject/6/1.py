import random

def throw_dice():
    return random.randint(1, 6)

while True:
    number = throw_dice()
    print("Silmäluku:", number)
    if number == 6:
        break
