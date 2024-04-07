from os import read
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
        headers = next(rows)
        for name, shares, price in rows:
            record = Stock(name, shares, price)
            records.append(record)
    return records