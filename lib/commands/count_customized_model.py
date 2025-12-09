from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from lib.database import print_cursor


def run(db: PooledMySQLConnection | MySQLConnectionAbstract, args):
    placeholders = ",".join(["%s"] * len(args.bmid_list))

    sql = f"""
    SELECT bm.bmid, bm.description, COUNT(cm.mid) AS customizedModelCount
    FROM cs122a.BaseModel bm
    LEFT JOIN cs122a.CustomizedModel cm ON bm.bmid = cm.bmid
    WHERE bm.bmid IN ({placeholders})
    GROUP BY bm.bmid, bm.description
    ORDER BY bm.bmid ASC
    """

    with db.cursor() as cursor:
        cursor.execute(sql, args.bmid_list)
        print_cursor(cursor)

    db.commit()
