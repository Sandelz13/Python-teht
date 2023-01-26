import random

number_of_dice = int(input("Kuinka monta arpakuutiota haluat heittää? "))

total = 0

for i in range(number_of_dice):
  roll = random.randint(1,6)
  total += roll

print("Silmälukujen summa on", total)