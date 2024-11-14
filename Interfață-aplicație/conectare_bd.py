import mysql.connector

#conectare la baza de date
def conectare():
    config = {
        'user': 'root',
        'password': 'password',
        'host': 'localhost',
        'database': 'cabinet',
        'port': '3306',
    }

    try:
        # conectare la serverul MySQL
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as error:
        print(error)



