import csv
import sys

def portfolio_cost(filename):
    cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                cost = cost + float(row[1])* float(row[2])
            except:
                print("Missing value in", row)
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

print('Total cost:', portfolio_cost(filename))
