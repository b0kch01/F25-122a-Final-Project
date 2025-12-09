from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection


def run(db: PooledMySQLConnection | MySQLConnectionAbstract, args):
    sql = """
    SELECT m.bmid, m.sid, i.provider, l.`domain` 
    FROM cs122a.LLMService l
    JOIN cs122a.InternetService i ON i.sid = l.sid 
    JOIN cs122a.ModelServices m ON m.sid = i.sid
    WHERE l.`domain` LIKE %s
    ORDER BY m.bmid;
    """

    with db.cursor() as cursor:
        cursor.execute(sql, (f"%{args.keyword}%",))
        print("\n".join(map(str, cursor.fetchall())))

    db.commit()
