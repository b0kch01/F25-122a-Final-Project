from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector import Error

def run(db: PooledMySQLConnection | MySQLConnectionAbstract, args):
    try:
        cursor = db.cursor()

        # Insert into users
        cursor.execute(
            """
            INSERT INTO Users (uid, email, username)
            VALUES (%s, %s, %s)
            """,
            (args.uid, args.email, args.username),
        )

        # Insert into AgentClient
        cursor.execute (
            """
            INSERT INTO AgentClient (
                uid,
                interests,
                cardholder,
                expire,
                cardno,
                cvv,
                zip
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                args.uid,
                args.interests,
                args.card_holder,
                args.expiration_date,
                args.card_number,
                args.cvv,
                args.zip,
            ),
        )

        db.commit()
        print("Success")
    
    except Error as e:
        db.rollback()
        print("Fail")
        print("DEBUG MYSQL ERROR: ", e)
    
    finally:
        cursor.close()
