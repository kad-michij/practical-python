# report.py
# Exercise 2.7

import csv

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) > 0:
                prices[row[0]] = float(row[1])
        return prices 

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price'  : float(row[2])
            }
            portfolio.append(holding)
    return portfolio

prices = read_prices('Work/Data/prices.csv')
portfolio = read_portfolio('Work/Data/portfolio.csv')
# print(prices)
# print(portfolio)

cost = 0.0
for s in portfolio:
    cost += s["shares"]*s["price"]

print('Total cost', cost)

value = 0.0
for s in portfolio:
    value += s["shares"]*prices[s["name"]]

print('Current value', value)
print('Gain', value - cost)

# Exercise 2.9
def make_report(portfolio, prices):
    report = []
    for r in portfolio:
        row = r['name'], r['shares'], prices[r['name']], (prices[r['name']]-r['price'])
        report.append(row)
    return report

report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * 4)
for r in report:
    print('%10s %10d %10.2f %10.2f' % r)

