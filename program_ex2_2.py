from pprint import pprint
from readrides import read_rides_as_dictionary

rows = read_rides_as_dictionary('python-mastery-main\\Data\\ctabus.csv')
route = '22'
date = '02/02/2011'

def bus_routes(lst_rows: list):
    lst_route = []
    for i in lst_rows:
        lst_route.append(i['route'])
    return len(set(lst_route))
    

def how_many_people_rode_bus(lst_rows: list, route: str, date: str):
    lst_passenger = []
    for i in lst_rows:
        if i['route'] == route and i['date'] == date:
            lst_passenger.append(i['rides'])
    return sum(lst_passenger)

def total_number_of_rides(lst_rows: list):
    _total_number_of_rides = {}
    for k in lst_rows:
        if k['route'] in _total_number_of_rides:
            _total_number_of_rides[k['route']].append(k['rides'])
        else:
            _total_number_of_rides[k['route']] = [k['rides']]
    total_sum_dct = {}
    for k in _total_number_of_rides:
        total_sum_dct[k] = sum(_total_number_of_rides[k])
    return total_sum_dct

def increase_in_the_number_of_passengers(lst_rows: list):
    _total_number_of_rides = {}
    for k in lst_rows:
        if 2000 < int(k['date'][-4:]) < 2012:
            if k['route'] in _total_number_of_rides:
                _total_number_of_rides[k['route']].append(k['rides'])
            else:
                _total_number_of_rides[k['route']] = [k['rides']]
    total_sum_dct = {}
    for k in _total_number_of_rides:
        total_sum_dct[k] = sum(_total_number_of_rides[k])
    sorted_total_sum_dct = sorted(total_sum_dct.items(), key=lambda x:x[1], reverse=True)
    convert_sort_dct = dict(sorted_total_sum_dct[:5])
    return convert_sort_dct

if __name__ == '__main__':
    # print(f'There are {bus_routes(rows)} bus routes in Chicago')
    # print(f'on {date}, {how_many_people_rode_bus(rows, route, date)} people were traveling by bus No. {route}')
    # pprint(total_number_of_rides(rows))
    # pprint(increase_in_the_number_of_passengers(rows))