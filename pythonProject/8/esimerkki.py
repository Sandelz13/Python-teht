import mysql.connector

def pelaajan_paikka(nimi):
    print("Ei ihan vielä valmis")
    return

def tulosta_pelaajat():
    sql = "SELECT screen_name, location " +\
          " FROM game"
    print(sql)
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()
    if cursor.rowcount >= 1:
        for rivi in tulos:
            print(f"Pelaaja: {rivi[0]} on paikassa: {rivi[1]}")
    return

yhteys = mysql.connector.connect(
        host='localhost',
        port= 3306,
        database='flight_game',
        user='user1',
        password='password1',
        autocommit=True
)

tulosta_pelaajat()

yhteys.close()