from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from lib.database import print_cursor


def run(db: PooledMySQLConnection | MySQLConnectionAbstract, args):
    sql = """
    SELECT a.uid, c.cid, c.labels, c.content, mc.duration
    FROM cs122a.ModelConfigurations mc 
    INNER JOIN cs122a.Configuration c ON c.cid = mc.cid
    INNER JOIN cs122a.AgentClient a ON a.uid = c.client_uid
    WHERE a.uid = %s
    ORDER BY mc.duration DESC
    LIMIT %s;
    """

    with db.cursor() as cursor:
        cursor.execute(sql, (args.uid, args.N))
        print_cursor(cursor)

    db.commit()
