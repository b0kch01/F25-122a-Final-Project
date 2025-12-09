import csv
from tabulate import tabulate
from textwrap import wrap

CELL_WIDTH = 25


def wrap_text(text):
    return "\n".join(wrap(text, width=CELL_WIDTH))


def wrap_items(row):
    return tuple(wrap_text(item) for item in row)


def run():
    with open("q9.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(map(wrap_items, reader))
        header, rows = rows[0], rows[1:]

    print(tabulate(rows, headers=header, tablefmt="grid"))
