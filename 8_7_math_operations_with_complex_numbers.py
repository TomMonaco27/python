"""
lesson 8 Task 7
Program "OperationComplex"
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата
"""


class OperationComplex:
    def __init__(self, real_part, imaginary_part):
        # complex real_part + (imaginary_part)i, где i^2 = -1
        self.real_part  = real_part
        self.imaginary_part = imaginary_part


    def __add__(self, other):
        #x1 + x2 + i(y1 + y2)
        self.result_add_real_part = self.real_part + other.real_part
        self.result_add_imaginary_part =  self.imaginary_part + other.imaginary_part
        return f'{self.result_add_real_part} + {self.result_add_imaginary_part}i'


print('Program "OperationComplex"')
a = OperationComplex(1,1)
b = OperationComplex(2,2)
print(a + b)
print('The end.')
