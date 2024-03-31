from readrides import read_rides_as_dictionary

rows = read_rides_as_dictionary('python-mastery-main\\Data\\ctabus.csv')

def bus_routes(lst_rows: list):
    lst_route = []
    for i in lst_rows:
        lst_route.append(i['route'])
    return len(set(lst_route))
    

def how_many_people_rode_bus(routes, date):
    pass

def total_number_of_rides():
    pass

def increase_in_the_number_of_passengers():
    pass

if __name__ == '__main__':
    print(f'There are {bus_routes(rows)} bus routes in Chicago')