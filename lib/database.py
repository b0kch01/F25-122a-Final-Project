import os
from typing import Sequence
from dotenv import load_dotenv

import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract, MySQLCursorAbstract
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.types import RowType


load_dotenv(".env.gradescope", override=True)
if os.path.exists(".env"):
    load_dotenv(".env", override=True)


def init_database():
    db = mysql.connector.connect(
        host="localhost",
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )
    return db


def print_cursor(cursor: MySQLCursorAbstract):
    for row in cursor.fetchall():
        for col_i, item in enumerate(row):
            print(item, end="")
            if col_i < len(row) - 1:
                print(",", end="")
        print()


def reset_database(db: PooledMySQLConnection | MySQLConnectionAbstract):
    cursor = db.cursor()

    cursor.execute("DROP DATABASE IF EXISTS `cs122a`;")
    cursor.execute("CREATE DATABASE `cs122a`;")
    cursor.execute("USE `cs122a`;")

    cursor.execute(
        """
    CREATE TABLE Users (
        uid INT,
        email TEXT NOT NULL,
        username TEXT NOT NULL,
        PRIMARY KEY (uid)
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE AgentCreator (
        uid INT,
        bio TEXT,
        payout TEXT,
        PRIMARY KEY (uid),
        FOREIGN KEY (uid) REFERENCES Users(uid) ON DELETE CASCADE
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE AgentClient (
        uid INT,
        interests TEXT NOT NULL,
        cardholder TEXT NOT NULL,
        expire DATE NOT NULL,
        cardno TEXT NOT NULL,
        cvv INT NOT NULL,
        zip INT NOT NULL,
        PRIMARY KEY (uid),
        FOREIGN KEY (uid) REFERENCES Users(uid) ON DELETE CASCADE
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE BaseModel (
        bmid INT,
        creator_uid INT NOT NULL,
        description TEXT NOT NULL,
        PRIMARY KEY (bmid),
        FOREIGN KEY (creator_uid) REFERENCES AgentCreator(uid) ON DELETE CASCADE
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE CustomizedModel (
        bmid INT,
        mid INT NOT NULL,
        PRIMARY KEY (bmid, mid),
        FOREIGN KEY (bmid) REFERENCES BaseModel(bmid) ON DELETE CASCADE
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE Configuration (
        cid INT,
        client_uid INT NOT NULL,
        content TEXT NOT NULL,
        labels TEXT NOT NULL,
        PRIMARY KEY (cid),
        FOREIGN KEY (client_uid) REFERENCES AgentClient(uid) ON DELETE CASCADE
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE InternetService (
        sid INT,
        provider TEXT NOT NULL,
        endpoints TEXT NOT NULL,
        PRIMARY KEY (sid)
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE LLMService (
        sid INT,
        domain TEXT,
        PRIMARY KEY (sid),
        FOREIGN KEY (sid) REFERENCES InternetService(sid) ON DELETE CASCADE
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE DataStorage (
        sid INT,
        type TEXT,
        PRIMARY KEY (sid),
        FOREIGN KEY (sid) REFERENCES InternetService(sid) ON DELETE CASCADE
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE ModelServices (
        bmid INT NOT NULL,
        sid INT NOT NULL,
        version INT NOT NULL,
        PRIMARY KEY (bmid, sid),
        FOREIGN KEY (bmid) REFERENCES BaseModel(bmid) ON DELETE CASCADE,
        FOREIGN KEY (sid) REFERENCES InternetService(sid) ON DELETE CASCADE
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE ModelConfigurations (
        bmid INT NOT NULL,
        mid INT NOT NULL,
        cid INT NOT NULL,
        duration INT NOT NULL,
        PRIMARY KEY (bmid, mid, cid),
        FOREIGN KEY (bmid, mid) REFERENCES CustomizedModel(bmid, mid) ON DELETE CASCADE,
        FOREIGN KEY (cid) REFERENCES Configuration(cid) ON DELETE CASCADE
    );
    """
    )

    cursor.close()
    db.commit()
