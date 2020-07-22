def portfolio_cost(filename):
    cost = 0.0
    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            try:
                cost = cost + float(row[1])* float(row[2])
            except:
                print("Missing value in", line)
    return cost

cost = portfolio_cost('Work/Data/missing.csv')
print('Total cost:', cost)
