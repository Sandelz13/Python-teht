from math import radians, cos, sin, asin, sqrt

# Define the coordinates of some example airports
airports = {
    "JFK": (40.6397, -73.7789),
    "LAX": (33.9416, -118.4085),
    "SFO": (37.7749, -122.4194),
    "ORD": (41.9786, -87.9048)
}

# Define a function to calculate the great circle distance between two points
def haversine_distance(lat1, lon1, lat2, lon2):
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

# Ask the user to choose the departure and arrival airports
print("Choose departure airport:")
for i, airport in enumerate(airports):
    print(f"{i+1}. {airport}")
departure_choice = int(input("Enter choice: "))
departure = list(airports.values())[departure_choice-1]

print("Choose arrival airport:")
for i, airport in enumerate(airports):
    if i+1 != departure_choice:
        print(f"{i+1}. {airport}")
arrival_choice = int(input("Enter choice: "))
arrival = list(airports.values())[arrival_choice-1]

# Calculate the distance between the departure and arrival airports
distance = haversine_distance(departure[0], departure[1], arrival[0], arrival[1])

# Assume a flying speed of 800 km/h
speed = 800

# Calculate the time consumed for the flight
time_consumed = distance / speed

# Print the result
print(f"The distance between {list(airports.keys())[departure_choice-1]} and {list(airports.keys())[arrival_choice-1]} is {distance:.2f} km.")
print(f"The time consumed for the flight at a speed of {speed} km/h is {time_consumed:.2f} hours.")

