
def print_table(lst:list, lst_name:list):
    '''printing the table according to the given list(lst_name) '''
    for i in lst_name:
        print(i.rjust(10), end=' ')
    print('')
    print(('-' * 10 + ' ') * len(lst_name))
    for i in lst:
        print(' '.join('%10s' % getattr(i, fieldname) for fieldname in lst_name))
