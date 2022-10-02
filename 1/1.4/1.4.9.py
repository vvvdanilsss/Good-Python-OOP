import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        return self.lst_data[a:b + 1]

    def insert(self, data):
        [self.lst_data.append(dict(zip(
            self.FIELDS, data[i].split()))) for i in range(len(data))]


db = DataBase()
db.insert(lst_in)