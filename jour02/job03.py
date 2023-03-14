import mysql.connector

db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='Laplateforme')
curseur = db.cursor()

curseur.execute("INSERT INTO etage(nom, numero, superficie) "
                "VALUES"
                "('RDC', 0, 500),"
                "('R+1', 1, 500)"
                )

curseur.execute("INSERT INTO salles(nom, id_etage, capacite)"
                "VALUES"
                "('Lounge', 1, 100),"
                "('Studio Son', 1, 5),"
                "('Broadcasting', 2, 50),"
                "('Bocal Peda', 2, 4),"
                "('Coworking', 2, 80),"
                "('Studio Video', 2, 5)"
                )


db.commit()

curseur.close()
db.close()