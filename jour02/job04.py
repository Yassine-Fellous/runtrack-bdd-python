import mysql.connector

db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='Laplateforme')
curseur = db.cursor()

curseur.execute("SELECT nom, capacite FROM salles")
result = curseur.fetchall()
print(result)

