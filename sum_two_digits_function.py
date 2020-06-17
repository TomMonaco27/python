"""
    Lesson 3 Task 3.
    Program "Sum of largest two numbers"
    Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
    аргументов.
"""


def my_func_2(arg_1, arg_2, arg_3):
    """
    Возвращает сумму наибольших двух элементов

    (number, number, number) -> number
    >>> my_func_2(2, 1, 3)
    5
    """
    list_2 = [arg_1, arg_2, arg_3]
    maxx_1 = list_2[0]
    for i in range(1, 2):
        if maxx_1 <= list_2[i]:
            maxx_1 = list_2[i]
    maxx_2 = max(list_2[1], list_2[2])
    sum_arg = [maxx_1, maxx_2]
    return sum(sum_arg)


print('Program "Sum of largest two numbers"')
print(f'Сумма двух наибольших элементов равна {my_func_2(10, 3, 10)}')
