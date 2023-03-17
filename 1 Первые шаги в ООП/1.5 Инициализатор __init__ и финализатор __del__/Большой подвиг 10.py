"""
Объявите два класса:

Cell - для представления клетки игрового поля;
GamePole - для управления игровым полем, размером N x N клеток.

С помощью класса Cell предполагается создавать отдельные клетки командой:

c1 = Cell(around_mines, mine)
Здесь around_mines - число мин вокруг данной клетки поля; mine - булева
величина (True/False), означающая наличие мины в текущей клетке. При этом,
в каждом объекте класса Cell должны создаваться локальные свойства:

around_mines - число мин вокруг клетки (начальное значение 0);
mine - наличие мины в текущей клетке (True/False);
fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально
все клетки закрыты (False).



С помощью класса GamePole должна быть возможность создавать квадратное игровое
поле с числом клеток N x N:

pole_game = GamePole(N, M)
Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка
представляется объектом класса Cell и все объекты хранятся в двумерном списке
N x N элементов - локальном свойстве pole объекта класса GamePole.

В классе GamePole должны быть также реализованы следующие методы:

init() - инициализация поля с новой расстановкой M мин (случайным образом по
игровому полю, разумеется каждая мина должна находиться в отдельной клетке).
show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если
клетка не открыта, то отображается символ #).

При создании экземпляра класса GamePole в его инициализаторе следует вызывать
метод init() для первоначальной инициализации игрового поля.

В классе GamePole могут быть и другие вспомогательные методы.

Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом
мин M = 12.

P.S. На экран в программе ничего выводить не нужно.
"""
from random import choices


class Cell:

    def __init__(self, mine, around_mines=0):
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = False


def count_mine(pole, len_pole):
    len_pole = len_pole + 2
    pole.insert(0, [0] * len_pole)
    pole.append([0] * len_pole)

    for _ in range(1, len_pole - 1):
        pole[_].insert(0, 0)
        pole[_].append(0)

    for i in range(1, len_pole - 1):
        for j in range(1, len_pole - 1):
            if pole[i][j] == '*':
                continue

            lst = pole[i - 1][j - 1: j + 2] + pole[i][j - 1: j + 2] + pole[i + 1][j - 1: j + 2]
            count_bomb = 0

            for case in lst:
                if case == '*':
                    count_bomb += 1
            pole[i][j] = count_bomb

    for _ in range(1, len_pole - 1):
        pole[_].pop(0)
        pole[_].pop(len_pole - 2)

    return pole[1:len_pole - 1]


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = []
        self.init()

    def init(self):
        len_pool = self.N * self.N
        lst_mine_id = choices(range(len_pool), k=self.M)
        pool = []

        for _ in range(len_pool):
            if _ in lst_mine_id:
                pool.append('*')
                continue
            pool.append(0)

        len_pole = self.N

        for i in range(len_pole):
            pole_line = []
            for j in range(len_pole):
                pole_line.append(pool.pop(0))
            self.pole.append(pole_line)

        self.pole = count_mine(self.pole, len_pole)

        for i in range(len_pole):
            for j in range(len_pole):
                if self.pole[i][j] == '*':
                    self.pole[i][j] = Cell(True)
                    continue
                self.pole[i][j] = Cell(False, self.pole[i][j])

    def show(self):
        for line in self.pole:
            for case in line:
                if not case.fl_open:
                    print('#', end=' ')
                    continue
                if case.mine:
                    print('*', end=' ')
                    continue
                print(case.around_mines, end=' ')
            print()


pole_game = GamePole(10, 12)