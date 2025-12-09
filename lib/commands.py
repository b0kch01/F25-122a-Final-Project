import os
import csv

from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from lib.database import reset_database


def importData(db: PooledMySQLConnection | MySQLConnectionAbstract, args):
    folder_name = args.folderName

    csv_files = []

    for entry in os.listdir(folder_name):
        full_path = os.path.join(folder_name, entry)
        if full_path.endswith(".csv") and os.path.isfile(full_path):
            csv_files.append((entry[: -len(".csv")], full_path))

    reset_database(db)

    cursor = db.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

    for entry, file_path in csv_files:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            rows = list(reader)

            cursor.executemany(
                f"""
                INSERT INTO {entry} VALUES ({",".join(["%s"]*len(header))});
                """,
                rows,
            )

    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    cursor.close()
    db.commit()
