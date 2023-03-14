class Dog:
    pass
num = 5

dog1 = Dog()
dog2 = Dog()

dog1.name = "Rekku"
dog2.name = "Ruffe"
dog1.weight = 6
dog2.weight = 7
print(f"1. koiran nimi {dog1.name},  paino: {dog1.weight} kiloa, ikä {dog1.age} vuotta")
print(f"2. koiran nimi {dog2.name}, paino: {dog2.weight} kiloa, ikä {dog2.age} vuotta")



###########################################



class Dog:

    dog_count = 0

    def __init__ (self, name, weight, age):
        Dog.dog_count += 1
        print(f"Uusi koira luotu, nimi: {name}")
        self.name = name
        self.weight = weight
        self.age = age
        self.energy_Level = 500 #0-1000
        self.distance = 0
    def eat(self):
        self.energy_Level = 100
        self.weight += 0.2

    def run(self, meters):
    while meters > 0 and self.energy_Level - metres * 0.1 >= 0:
        meters -= 1
        self.distance = self.distance + 1
        self.energy_Level = self.energy_Level - 0.1


    def say_hello(self):
         print(f"Hei olen {self.name}")
            f"paino: {self.weight} kg, ikä: {self.age} vuotta"
            f"energiaa jäljellä {self.energy_Level}"

dog1 = Dog("Rekku", 5, 2)
dog2 = Dog("Ruffe", 8, 12)
dog1.eat()
dog2.eat()
dog1.say_hello()
dog2.say_hello()
dog3 = Dog("Muro", 12, 10);
dog1.run(200)
dog2.run(500)
dog1.name = "Rekku"
dog2.name = "Ruffe"
dog1.weight = 6
dog2.weight = 7

print(f"Koria luotu yheensä: {Dog.dog_count}")


print(f"1. koiran nimi {dog1.name},  paino: {dog1.weight} kiloa, ikä {dog1.age} vuotta")
print(f"2. koiran nimi {dog2.name}, paino: {dog2.weight} kiloa, ikä {dog2.age} vuotta")

dogs = []
for i in range (5):
    dogs.append(Dog("Koira"))