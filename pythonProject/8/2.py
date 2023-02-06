import mysql.connector

def get_airport_count(country_code):
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='user1',
        password='password1',
        autocommit=True
    )

    cursor = conn.cursor()


    query = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type"
    cursor.execute(query, (country_code,))


    results = cursor.fetchall()


    for result in results:
        print("Haulla {} löytyy kenttiä: {} kappaletta".format(result[0], result[1]))

    cursor.close()
    conn.close()

country_code = input("Anna maakoodi: ")

get_airport_count(country_code)