#!./venv/bin/python

import mysql.connector
import argparse

db = mysql.connector.connect(host="localhost", username="root", password="12345678")

parser = argparse.ArgumentParser(
    prog="project.py", description="122a Final Project CLI for Agent Platform"
)


if __name__ == "__main__":
    args = parser.parse_args()
