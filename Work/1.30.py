def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost

cost = portfolio_cost('Work/Data/portfolio.csv')
print('Total cost:', cost)

