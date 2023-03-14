class Car:
    def __init__(self, reg_number, top_speed, current_speed, distance_travelled):
        self.reg_number = reg_number
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.distance_travelled= distance_travelled

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed > self.top_speed:
            self.current_speed = self.top_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

distance_travelled = 0
current_speed = 0
car1 = Car("ABC-123", 142, current_speed, distance_travelled)

print(f"1. auton rekisterinumero {car1.reg_number}, huippunopeus {car1.top_speed} kmh, tämän hetkinen nopeus {car1.current_speed}, ja matka kuljettu {car1.distance_travelled } ")


car = Car("ABC-123", 180, 0, 0)

car.accelerate(30)
print("Auton nopeus:", car.current_speed)

car.accelerate(70)
print("Auton nopeus:", car.current_speed)

car.accelerate(50)
print("Auton nopeus:", car.current_speed)

car.accelerate(-200)
print("Auton nopeus hätäjarrutuksen jälkeen:", car.current_speed)