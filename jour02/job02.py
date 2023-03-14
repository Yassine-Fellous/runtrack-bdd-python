import mysql.connector

db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='Laplateforme')
curseur = db.cursor()

curseur.execute("CREATE TABLE etage ("
                "id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,"
                "nom VARCHAR(255),"
                "numero INT NOT NULL,"
                "superficie INT NOT NULL"
                ")")

curseur.execute("CREATE TABLE salles ("
                "id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,"
                "nom VARCHAR(255),"
                "id_etage INT NOT NULL,"
                "capacite INT NOT NULL"
                ")")
