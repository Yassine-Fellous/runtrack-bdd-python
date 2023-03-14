import mysql.connector

db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='Laplateforme')
curseur = db.cursor()

curseur.execute("SELECT * FROM etudiants")
result = curseur.fetchall()
print(result)
