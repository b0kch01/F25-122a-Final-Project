from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection


def run(db: PooledMySQLConnection | MySQLConnectionAbstract, args):
    sql = """
    SELECT c.client_uid, c.cid , c.content, mc.duration
    FROM main.ModelConfigurations mc 
    INNER JOIN main.Configuration c ON c.cid = mc.cid
    WHERE c.client_uid = %s
    ORDER BY mc.duration DESC
    LIMIT %s;
    """

    cursor = db.cursor()
    cursor.execute(sql, (args.uid, args.N))

    print("\n".join(map(str, cursor.fetchall())))
