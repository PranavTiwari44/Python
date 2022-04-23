import csv

csv_file = 'OlympicMedals_2020.csv'

with open(csv_file, encoding='utf-8', newline='') as readfile:
    reader = csv.reader(readfile)
    next(reader)
    for row in reader:
        print(row)

