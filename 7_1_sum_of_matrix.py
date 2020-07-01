"""
Lesson 7 Task 1.
Program sum and print two Matrix
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, list_of_lists):
        try:
            self.list_of_lists = list_of_lists
            self.final_matrix = [[0 for i in range(len(self.list_of_lists[0]))] for j in range(len(self.list_of_lists))]
        except:
            print('Error __init__')

            
    def __str__(self):
        try:
            return '\n'.join('\t'.join(map(str, row)) for row in self.list_of_lists)
        except:
            print('Error __str__')

            
    def __add__(self, other):
        try:
            for i in range(len(self.list_of_lists)):
                for j in range(len(self.list_of_lists[0])):
                    self.final_matrix[i][j] = self.list_of_lists[i][j] + other.list_of_lists[i][j]
            return self.final_matrix
        except:
            print('Error in __add__()')


print('Program sum and print two Matrix')
my_matrix_1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
my_matrix_2 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(my_matrix_1)
print()
print(my_matrix_2)
print()
mat = my_matrix_1 + my_matrix_2
my_Matrix_3 = Matrix(mat)
print(my_Matrix_3)
