import csv


class Stock:
    _types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def __repr__(self):
         return f'{type(self).__name__}({self.name!r},{self.shares!r},{self.price!r})'

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) == 
                                             (other.name, other.shares, other.price))

    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        self.shares -= nshares
    
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

def read_portfolio(filename:str):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # noqa: F841
        for row in rows:
            record = Stock.from_row(row)
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