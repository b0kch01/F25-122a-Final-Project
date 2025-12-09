from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector import Error

def run (db: PooledMySQLConnection | MySQLConnectionAbstract, args):
    try:
        cursor = db.cursor()
        cursor.execute("USE main;")
        cursor.execute (
            """
            INSERT INTO CustomizedModel (bmid, mid)
            VALUES (%s, %s)
            """,
            (args.bmid, args.mid),
        )

        db.commit()
        print("Success")

    except Error as e:
        db.rollback()
        print("Fail")
        print(e)
    
    finally:
        cursor.close()
