from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection


def run(db: PooledMySQLConnection | MySQLConnectionAbstract, args):
    sql = """
    SELECT s.sid, s.endpoints, s.provider
    FROM main.InternetService s
    JOIN main.ModelServices ms ON ms.sid = s.sid
    WHERE ms.bmid = %s
    ORDER BY s.provider ASC
    """

    with db.cursor() as cursor:
        cursor.execute(sql, (args.bmid,))
        print("\n".join(map(str, cursor.fetchall())))

    db.commit()
