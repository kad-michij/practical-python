import csv


def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if len(row) > 0:
                prices[row[0]] = row[1]
            #     print(prices)    
            # try:
            #     prices = {row[0] : row[1]}
            #     print(prices)
            # except:
            #     print("Error")
        return prices

# from pprint import pprint
# pprint(read_prices('Work/Data/prices.csv'))
print(read_prices('Work/Data/prices.csv'))
