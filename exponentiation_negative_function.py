"""
Lesson 3 Task 4.
Program "Exponentiation negative function"
Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора # **, предусматривающая использование цикла.
"""


def my_func(x, y):
    while x < 0:
        x = int(input('Enter only positive number: '))
    while y > 0:
        y = int(input('Enter only negative number: '))
    exponentiation = 1 / (x ** abs(y))
    return f'Exponentiation negative = {exponentiation}, wiht use pow = {pow(x, y)}'  # pow(x, y) - для проверки правильности вычислений


print(my_func(x=int(input('Enter positive number: ')), y=int(input('Enter negative number: '))))


# -----------------------------------------------------------2----------------------------------------------------------


def my_func_1(x_1, y_1):
    exponentiation_1 = 1
    for i in range(1, abs(y_1) + 1):
        exponentiation_1 = exponentiation_1 * x_1
    return 1 / exponentiation_1


print(my_func_1(x_1=int(input('Enter positive number: ')), y_1=int(input('Enter negative number: '))))
