#!./venv/bin/python

import mysql.connector
import argparse


def init_database():
    db = mysql.connector.connect(host="localhost", username="root", password="12345678")

    return db


def parse_args():
    parser = argparse.ArgumentParser(
        prog="project.py", description="122a Final Project CLI for Agent Platform"
    )

    function_subparser = parser.add_subparsers(dest="function", required=True)

    # IMPORT
    import_parser = function_subparser.add_parser(
        "import", help="Imports data in a given directory. Deletes existing tables."
    )
    import_parser.add_argument("folder_name", type=str)

    # INSERT AGENT
    insert_agent_parser = function_subparser.add_parser(
        "insertAgentClient", help="Insert a new agent client into the related tables."
    )
    insert_agent_parser.add_argument("uid", type=int)
    insert_agent_parser.add_argument("username", type=str)
    insert_agent_parser.add_argument("email", type=str)
    insert_agent_parser.add_argument("card_number", type=int)
    insert_agent_parser.add_argument("card_holder", type=str)
    insert_agent_parser.add_argument("expiration_date", type=str)
    insert_agent_parser.add_argument("cvv", type=int)
    insert_agent_parser.add_argument("zip", type=int)
    insert_agent_parser.add_argument("interests", type=str)

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    match args.function:
        case "import":
            pass
