import math

def calculate_pizzas_unit_price(diameter, price):
    pi = math.pi
    area = pi * (diameter/2)**2
    unit_price = price / area
    return unit_price

def main():
    pizza1_diameter = float(input("Syötä 1. pizzan halkaisija senttimetreinä: "))
    pizza1_price = float(input("Syötä 1. pizzan hinta euroina: "))
    pizza2_diameter = float(input("Syötä 2. pizzan halkaisija senttimetreinä: "))
    pizza2_price = float(input("Syötä 2. pizzan hinta euroina: "))

    pizza1_unit_price = calculate_pizzas_unit_price(pizza1_diameter, pizza1_price)
    pizza2_unit_price = calculate_pizzas_unit_price(pizza2_diameter, pizza2_price)

    if pizza1_unit_price < pizza2_unit_price:
        print("1. pizza tarjoaa paremman vastineen rahalle.")
    elif pizza1_unit_price > pizza2_unit_price:
        print("2. pizza tarjoaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizzat tarjoavat yhtä hyvän vastineen rahalle.")

if __name__ == "__main__":
    main()