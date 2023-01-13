# Kolminumeroinen 1-9 koodi
import random

numero = random.randint(1, 999)
print("Kolminumeroinen 1-9 koodisi on:", numero)


# Nelinumeroinen 1-6 koodi

import random

Koodi = ['1','2','3','4','5','6']

q_list = [random.choice(Koodi) for i in range(4)]
print("Nelinumeroinen 1-6 koodisi on", q_list)


