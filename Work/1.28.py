import gzip

with gzip.open('Work/Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')
