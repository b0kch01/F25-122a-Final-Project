import csv


def print_row(row):
    print(",".join(row))


def run():
    with open("q9.csv", "r") as file:
        print(file.read())
