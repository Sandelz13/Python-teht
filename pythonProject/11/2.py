class Car:
    def __init__(self, reg_number, top_speed, current_speed=0, distance_travelled=0):
        self.reg_number = reg_number
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.distance_travelled = distance_travelled

    def drive(self, time):
        self.distance_travelled += self.current_speed * time

class Sähköauto(Car):
    def __init__(self, reg_number, top_speed, battery_capacity, current_speed=0, distance_travelled=0):
        super().__init__(reg_number, top_speed, current_speed, distance_travelled)
        self.battery_capacity = battery_capacity

class Polttomoottoriauto(Car):
    def __init__(self, reg_number, top_speed, fuel_tank_size, current_speed=0, distance_travelled=0):
        super().__init__(reg_number, top_speed, current_speed, distance_travelled)
        self.fuel_tank_size = fuel_tank_size

electric_car = Sähköauto("ABC-15", 180, 52.5)
gas_car = Polttomoottoriauto("ACD-123", 165, 32.3)

electric_car.current_speed = 120
gas_car.current_speed = 140

driving_time = 3
electric_car.drive(driving_time)
gas_car.drive(driving_time)

print("Sähköauton matkamittarilukema:", electric_car.distance_travelled)
print("Polttomoottoriauton matkamittarilukema:", gas_car.distance_travelled)
