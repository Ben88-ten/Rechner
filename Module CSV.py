import csv
with open("fromexel.csv",newline = '') as file:
    csv_file = csv.reader(file, delimiter = ",")
    for line in csv_file:
        print(line)