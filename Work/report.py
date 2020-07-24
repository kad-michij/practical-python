# report.py
#
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

cost = 0.0
for s in portfolio:
    cost += s["shares"]*s["price"]

print('Total cost', cost)

value = 0.0
for s in portfolio:
    value += s["shares"]*prices[s["name"]]

print('Current value', value)
print('Gain', value - cost)

