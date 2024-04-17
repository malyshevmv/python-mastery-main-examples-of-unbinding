from abc import ABC, abstractmethod

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()

    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))
    
    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end=' ')
        for i in headers:
            print(f'<tr>{i}</tr>', end=' ')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end=' ')
        for i in rowdata:
            print(f'<tr>{i}</tr>', end=' ')
        print('</tr>')

class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])

def create_formatter(name: str, column_formats=None, upper_headers=True):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'unknow format {name}')
    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass
    return formatter_cls()
        

def print_table(lst:list, lst_name:list, formatter):
    '''printing the table according to the given list(lst_name) '''
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')
    formatter.headings(lst_name)
    #for i in lst_name:
    #    print(i.rjust(10), end=' ')
    #print('')
    #print(('-' * 10 + ' ') * len(lst_name))
    for i in lst:
        #print(' '.join('%10s' % getattr(i, fieldname) for fieldname in lst_name))
        rowdata = [getattr(i, fieldname) for fieldname in lst_name]
        formatter.row(rowdata)