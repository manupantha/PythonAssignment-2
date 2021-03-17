import csv


def csv_read():
    with open("filename.csv", 'r') as file:
        reader = csv.DictReader(file)
        result = list(reader)
        print(result)


csv_read()
