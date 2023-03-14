class Car:
    def __init__(self, reg_number, top_speed, current_speed, distance_travelled):
        self.reg_number = reg_number
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.distance_travelled = distance_travelled


distance_travelled = 0
current_speed = 0
car1 = Car("ABC-123", 142, current_speed, distance_travelled)

print(
    f"1. auton rekisterinumero {car1.reg_number}, huippunopeus {car1.top_speed} kmh, tämän hetkinen nopeus {car1.current_speed}, ja matka kuljettu {car1.distance_travelled} ")
