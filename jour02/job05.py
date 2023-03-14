import mysql.connector

db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='Laplateforme')
curseur = db.cursor()

curseur.execute("SELECT SUM(superficie) FROM etage")
result = curseur.fetchone()[0]
print("La superficie de La Plateforme est de", str(result), "m2")

db.commit()

curseur.close()
db.close()