import mysql.connector

db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='Laplateforme')
curseur = db.cursor()

curseur.execute("CREATE TABLE employes("
                "id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,"
                "nom VARCHAR NOT NULL,"
                "prenom VARCHAR NOT NULL,"
                "salaire DECIMAL NOT NULL,"
                "id_service INT NOT NULL)")

curseur.execute("INSERT INTO employes(nom, prenom, salaire, id_service)"
                "VALUES"
                "('jean', 'fini', 100000, 1),"
                "('marck', 'fini', 10000, 2),"
                "('paul', 'fini', 2, 50)"
                )

db.commit()
curseur.close()
db.close()