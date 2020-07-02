"""
lesson 7 task 3
program "Cell order"
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
 сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
 Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
  обычное (не целочисленное) деление клеток, соответственно.
  В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
 иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
 Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
 Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
 Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке:
 https://pythonworld.ru/osnovy/peregruzka-operatorov.html.
"""


class Cell:
    def __init__(self, number_cells):
        self.number_cells = number_cells

    def __add__(self, other):
        try:
            self.final_cell = self.number_cells + other.number_cells
            return f'Cell: {self.number_cells} + Cell: {other.number_cells} result: {self.final_cell}'
        except:
            print('Error __add__')

    def __sub__(self, other):
        try:
            self.final_cell = max(self.number_cells, other.number_cells) - min(self.number_cells, other.number_cells)
            if self.final_cell >= 0:
                return f'Cell: {max(self.number_cells, other.number_cells)} - Cell: {min(self.number_cells, other.number_cells)} result: {self.final_cell}'
            else:
                return f'Разница меньше нуля'
        except:
            print('Error __sub__')

    def __mul__(self, other):
        try:
            self.final_cell = self.number_cells * other.number_cells
            return f'Cell: {self.number_cells} * Cell: {other.number_cells} result: {self.final_cell}'
        except:
            print('Error __mul__')

    def __truediv__(self, other):
        try:
            self.final_cell = max(self.number_cells, other.number_cells) // min(self.number_cells, other.number_cells)
            return f'Cell: {max(self.number_cells, other.number_cells)} // Cell: {min(self.number_cells, other.number_cells)} result: {self.final_cell}'
        except:
            print('Error __truediv__')

    def __str__(self):
        return f'Cell: {self.number_cells}'

    def make_order(self, num_cells_in_row):
        try:
            print('\nMake order: ')
            count_cells = divmod(self.number_cells, num_cells_in_row)
            for i in range(count_cells[0]):
                print('*' * num_cells_in_row, end='')
                print('')
            for j in range(count_cells[1]):
                print('*', end='')
        except:
            print('Error make_order()')


print('Program "Cell order"')
a = Cell(22)
b = Cell(11)
print(a)
print(a+b)
print(a-b)
print(b-a)
print(a*b)
print(b / a)
c = Cell(10)
c.make_order(3)
c.make_order(5)
c.make_order(8)
