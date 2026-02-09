import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='hade',
    password='New_password.',
    autocommit=True
)

icao_code = input("Enter the ICAO code of an airport: ").upper()


def hae_data():
    sql = "Select ident, name, municipality FROM airport LIMIT 10"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        print(f"No airport found with ICAO code {icao_code}")
    return


hae_data()


while True:
    icao_code = hae_data()
else:
    print(f"No airport found with ICAO code {icao_code}")
