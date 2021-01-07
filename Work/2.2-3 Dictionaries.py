import csv
f = open('Work/Data/portfolio.csv')
rows = csv.reader(f)
next(rows)
row = next(rows)
# print(row)

d = {
        'name' : row[0],
        'shares' : int(row[1]),
        'price'  : float(row[2])
    }
print(d)

cost = d['shares'] * d['price']
print(cost)

d['shares'] = 75
d['date'] = (6, 11, 2007)
d['account'] = 12345
print(d)

# print(list(d)) -> alleen keys slaat die dan op

for k in d:
    print("k=", k)

for k in d:
    print(k, "=", d[k])

keys = d.keys()
print(keys)
del d["account"]
print(keys)

items = d.items()
print(items)

d = dict(items)
print(d)

