import os
import csv


def importData(db, args):
    folder_name = args.folderName

    csv_files = []

    for entry in os.listdir(folder_name):
        full_path = os.path.join(folder_name, entry)
        if full_path.endswith(".csv") and os.path.isfile(full_path):
            csv_files.append(full_path)

    for file_path in csv_files:
        with open(file_path, "r") as file:
            reader = csv.reader(file)

            header = next(reader)

            for row in reader:
                print(row)

                return
