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

distance_travelled = 2000
current_speed = 0
car1 = Car("ABC-123", 142, current_speed, distance_travelled)

print(f"1. auton rekisterinumero {car1.reg_number}, huippunopeus {car1.top_speed} kmh, tämän hetkinen nopeus {car1.current_speed}, ja matka kuljettu {car1.distance_travelled } ")


car1.accelerate(30)
print("Auton nopeus:", car1.current_speed)

car1.accelerate(70)
print("Auton nopeus:", car1.current_speed)

car1.accelerate(50)
print("Auton nopeus:", car1.current_speed)

car1.accelerate(-200)
print("Auton nopeus hätäjarrutuksen jälkeen:", car1.current_speed)

car1.accelerate(60)

print(f"Nopeus: {car1.current_speed} km/h")
print(f"Kuljettu matka: {car1.distance_travelled} km")

car1.travel(1.5)

print(f"Kuljettu matka: {car1.distance_travelled} km")


car_list = []
for i in range(1, 11):
    reg_number = "ABC-" + str(i)
    top_speed = random.randint(100, 200)
    new_car = Car(reg_number, top_speed, current_speed=0, distance_travelled=0)
    car_list.append(new_car)


kilometers = 0
while True:
    for car in car_list:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.travel(1)
        if car.distance_travelled >= 10000:
            kilometers = 10000
            break
    if kilometers == 10000:
        break


print("Kisa päättyi!")
print("Autot ja niiden tiedot:")
print("{:<10} {:<15} {:<10} {:<15}".format("Reg. no.", "Huippunopeus(km/h)", "Tämän hetkinen nopeus (km/h)", "Matka (km)"))
for car in car_list:
    print("{:<10} {:<15} {:<10} {:<15}".format(car.reg_number, car.top_speed, car.current_speed, car.distance_travelled))