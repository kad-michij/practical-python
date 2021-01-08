import csv

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

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)