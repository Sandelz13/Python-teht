import random

N = 1000000
counter = 0
n = 0
while counter < N:
    counter += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    # print(f"arvotty piste {x}, {y}")
    # onko piste yksikköympyrän sisällä: x^2+y^2<1
    # print(f"{x * x + y * y < 1}")
    if x * x + y * y < 1:
        # print("on sisällä")
        n += 1
print(f"Pisteitä arvottu yhteensä {counter}, joista {n} kpl ympyrän sisällä")
print("Piin likiarvo on", 4*n/N)


