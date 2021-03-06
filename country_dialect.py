import csv

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = countries_data.read()
    country_dialect = csv.Sniffer().sniff(sample)
    countries_data.seek(0)
    country_dialect.skipinitialspace= True
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)
