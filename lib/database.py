import mysql.connector


def init_database():
    db = mysql.connector.connect(host="localhost", username="root", password="12345678")

    return db
