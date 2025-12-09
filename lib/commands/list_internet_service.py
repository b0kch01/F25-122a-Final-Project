from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from lib.database import print_cursor


def run(db: PooledMySQLConnection | MySQLConnectionAbstract, args):
    sql = """
    SELECT s.sid, s.endpoints, s.provider
    FROM cs122a.InternetService s
    JOIN cs122a.ModelServices ms ON ms.sid = s.sid
    WHERE ms.bmid = %s
    ORDER BY s.provider ASC
    """

    with db.cursor() as cursor:
        cursor.execute(sql, (args.bmid,))
        print_cursor(cursor)

    db.commit()
