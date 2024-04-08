import csv


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price

def read_portfolio(filename:str):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # noqa: F841
        for name, shares, price in rows:
            record = Stock(name, int(shares), float(price))
            records.append(record)
    return records

def print_portfolio(lst:list):
     print(f'{"name".rjust(10)}{"shares".rjust(10)}{"price".rjust(10)}')
     print('---------- ' * 3)
     for s in lst:
          print(f'{s.name.rjust(10)} {s.shares:10} {s.price:10.2f}')

if __name__ == '__main__':
    p = read_portfolio('E:\\python\\python-mastery-main\\python-mastery-main\\Data\\portfolio.csv')
    for s in p:
	    print(f'{s.name.rjust(5)} {s.shares:5} {s.price:.2f}')