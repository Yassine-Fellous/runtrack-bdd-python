import mysql.connector

db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='Laplateforme')
curseur = db.cursor()

curseur.execute("SELECT SUM(capacite) FROM salles")
result = curseur.fetchone()[0]
print("La capacité de toute les salles est de :", str(result))

db.commit()

curseur.close()
db.close()