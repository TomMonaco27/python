"""
Lesson 4 Task 5
Program "Multiply of all elements with use reduce() function"
Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов
списка. Подсказка: использовать функцию reduce().
"""

from functools import reduce


print('Program "Multiplications of all elements with use reduce() function"')
new_list_2 = [el for el in range(100, 1001) if el % 2 == 0]
multiply_all = reduce(lambda x,y: x * y, new_list_2)
print(f'Starting list is: {new_list_2}')
print(f'Multiply of all elements in starting list: {multiply_all}')

# ----------------------------------------------------------2-----------------------------------------------------------


def multiply_all_el(new_list_2):
    multiply_all = reduce(lambda x, y: x * y, new_list_2)
    print(f'Multiply of all elements in starting list: {multiply_all}')


print(f'\nStarting list is: {new_list_2}')
multiply_all_el(new_list_2)
