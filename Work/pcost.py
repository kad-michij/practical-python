# pcost.py
#
# Exercise 1.27

cost = 0.0


# with open('Data/portfolio.csv', 'rt') as f:
#     headers = next(f)
#     for line in f:
#         row = line.split(',')
#         cost = cost + float(row[1])* float(row[2])

# print("Total cost", cost)

#Exercise 2.15
import csv
with open('Data/missing.csv', 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for rowno, row in enumerate(rows, start=1):
        try:
            cost = cost + float(row[1])* float(row[2])
        except ValueError:
            print(f'Row {rowno}: "Couldn\'t convert" Bad row: {row}')
 
print("Total cost", cost)

