import csv

fileName = "data.csv"
fields = []
rows = []

with open(fileName,'r') as csv_test:
    csvreader = csv.reader(csv_test)

    fields=next(csvreader)

    for row in csvreader:
        rows.append(row)

    print("Total number of rows are: %d"%csvreader.line_num)
    row_count = csvreader.line_num
print('Total names are '+','.join(field for field in fields))

for row in rows[:row_count]:
    for col in rows:
        print('%8s'%col, end="")
    print("\n")
