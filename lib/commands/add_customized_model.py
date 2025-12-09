from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector import Error


def run(db: PooledMySQLConnection | MySQLConnectionAbstract, args):
    cursor = db.cursor()

    try:
        cursor.execute("USE cs122a;")
        cursor.execute(
            """
            INSERT INTO CustomizedModel (bmid, mid)
            VALUES (%s, %s)
            """,
            (args.bmid, args.mid),
        )

        db.commit()
        print("Success")

    except Error:
        db.rollback()
        print("Fail")

    finally:
        cursor.close()
