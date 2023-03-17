"""
Объявите класс TriangleChecker, объекты которого можно было бы создавать
командой:

tr = TriangleChecker(a, b, c)
Здесь a, b, c - длины сторон треугольника.

В классе TriangleChecker необходимо объявить метод is_triangle(), который
бы возвращал следующие коды:

1 - если хотя бы одна сторона не число (не float или int) или хотя бы
одно число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.

Проверку параметров a, b, c проводить именно в таком порядке.

Прочитайте из входного потока строку, содержащую три числа, разделенных
пробелами, командой:

a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему
прочитанные значения a, b, c. Вызовите метод is_triangle() из объекта
tr и выведите результат на экран (код, который она вернет).
"""


class TriangleChecker:

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def is_triangle(self):
        for x in (self.a, self.b, self.c):
            if type(x) not in (int, float) or x <= 0:
                return 1
        if self.a + self.b <= self.c or self.c + self.a <= self.b or self.b + self.c <= self.a:
            return 2
        else:
            return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())