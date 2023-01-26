numbers = []

while True:
    number = input("Anna luku tai jätä kenttä tyhjäksi lopettaaksesi: ")
    if number == "":
        break
    numbers.append(int(number))

numbers.sort(reverse=True)
print("Viisi suurinta antamaasi lukua:")
for i in range(5):
    if i < len(numbers):
        print(numbers[i])