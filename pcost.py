def portfolio_cost(filename: str):
    total_amount = 0.0
    with open(filename, 'r') as portfolio:
        for line in portfolio:
            port_lst = line.split()
            try:
                number_of_shares = int(port_lst[1])
            except ValueError as err:
                print(err)
            try:
                price_of_shares = float(port_lst[2])
            except ValueError as err:
                print(err)
            total_amount += number_of_shares * price_of_shares
    return total_amount

if __name__ == '__main__':
    print(portfolio_cost('E:\\python\\python-mastery-main\\python-mastery-main\\Data\\portfolio3.dat'))