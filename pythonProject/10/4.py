import random

class Car:
    def __init__(self, reg_number, top_speed, current_speed=0, distance_travelled=0):
        self.reg_number = reg_number
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.distance_travelled = distance_travelled

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed > self.top_speed:
            self.current_speed = self.top_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def travel(self, time):
        distance = self.current_speed * time
        self.distance_travelled += distance

class Race:
    def __init__(self, name, length, car_list):
        self.name = name
        self.length = length
        self.car_list = car_list

    def tunti_kuluu(self):
        for car in self.car_list:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.travel(1)

    def tulosta_tilanne(self):
        print("{:<10} {:<15} {:<10} {:<15}".format("Reg. no.", "Huippunopeus(km/h)", "Tämän hetkinen nopeus (km/h)", "Matka (km)"))
        for car in self.car_list:
            print("{:<10} {:<15} {:<10} {:<15}".format(car.reg_number, car.top_speed, car.current_speed, car.distance_travelled))

    def kilpailu_ohi(self):
        for car in self.car_list:
            if car.distance_travelled >= self.length:
                return True
        return False


car_list = []
for i in range(1, 11):
    reg_number = "ABC-123-" + str(i)
    top_speed = random.randint(100, 200)
    new_car = Car(reg_number, top_speed, current_speed=0, distance_travelled=0)
    car_list.append(new_car)

suuri_romuralli = Race("Suuri romuralli", 8000, car_list)

print("Kilpailu: " + suuri_romuralli.name)
print("Pituus: " + str(suuri_romuralli.length) + " km")
print("Osallistuvat autot:")
for car in suuri_romuralli.car_list:
    print(car.reg_number)

print("\nKilpailu alkaa!")
hour = 1
while not suuri_romuralli.kilpailu_ohi():
    suuri_romuralli.tunti_kuluu()
    if hour % 10 == 0:
        print(f"Tunti {hour}:")
        suuri_romuralli.tulosta_tilanne()
    hour += 1

print("\nKilpailu ohi!")
suuri_romuralli.tulosta_tilanne()
