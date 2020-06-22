"""
Lesson 4 Task 7
Program "Factorial function with yield use"
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def fact(n):
    factorial_n = 1
    for i in range(1, n + 1):
        factorial_n *= i
        yield factorial_n


i = 0

print('Program "Factorial function with yield use"')
n = int(input('Enter a number for calculating to n-factorial: '))
for el in fact(n):
    i += 1
    print(f'Factorial {i}! =  {el}')
