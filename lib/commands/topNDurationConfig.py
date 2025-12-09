from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection


def run(db: PooledMySQLConnection | MySQLConnectionAbstract, args):
    

