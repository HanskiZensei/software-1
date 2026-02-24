import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='hade',
    password='New_password.',
    autocommit=True
)


def hae_data():
    sql = "Select * FROM goal"

    kursori = yhteys.cursor()
    kursori.execute(sql)

    tulos = kursori.fetchall()

    print(tulos)
    print(tulos[0])
    print(tulos[0][0])

    for rivi in tulos:
        print(rivi)

        for alkio in rivi:
            print("  ", alkio)


hae_data()