import mysql.connector
from geopy.distance import great_circle

def get_distance(icao1, icao2):
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='user1',
        password='password1',
        autocommit=True
    )

    cursor = conn.cursor()

    query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(query, (icao1,))
    result = cursor.fetchone()
    lat1, lon1 = result

    query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(query, (icao2,))
    result = cursor.fetchone()
    lat2, lon2 = result

    distance = great_circle((lat1, lon1), (lat2, lon2)).km

    print("Etäisyys {} ja {} välillä on {:.2f} km".format(icao1, icao2, distance))

    cursor.close()
    conn.close()

icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-koodi: ")

get_distance(icao1, icao2)
