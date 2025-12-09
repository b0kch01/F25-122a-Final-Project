from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector import Error


def run(db: PooledMySQLConnection | MySQLConnectionAbstract, args):
    cursor = db.cursor()
    try:
        cursor.execute(
            """
            SELECT *
            FROM cs122a.User
            WHERE uid = %s AND email = %s AND username = %s;
            """,
            (args.uid, args.email, args.username),
        )

        if cursor.fetchone() is None:
            # Insert into users
            cursor.execute(
                """
                INSERT INTO cs122a.User (uid, email, username)
                VALUES (%s, %s, %s)
                """,
                (args.uid, args.email, args.username),
            )

        # Insert into AgentClient
        cursor.execute(
            """
            INSERT INTO cs122a.AgentClient (
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

    except Error:
        db.rollback()
        print("Fail")

    finally:
        cursor.close()
