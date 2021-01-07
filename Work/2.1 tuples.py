import csv
f = open('Data/portfolio.csv')
rows = csv.reader(f)
next(rows)
row = next(rows)
print(row)

t = (row[0], int(row[1]), float(row[2]))
print(t)
cost = t[1] * t[2]
print(cost)
t = (t[0], 75, t[2])
print(t)

name, shares, price = t
print(name)
t = (name, 2*shares, price)
print(t)