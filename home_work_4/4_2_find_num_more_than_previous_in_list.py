"""
Lesson 4 Task 2
Program "find numbers more than previous in the list"
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


import random

new_list_1 = []
new_list_2 = []
new_list_3 = [el for el in range((random.randint(1, 100)))]
random.shuffle(new_list_3)
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [my_list[num_el] for num_el in range(1, len(my_list)) if my_list[num_el] > my_list[(num_el - 1)]]
print('\nProgram "Find numbers more than previous in the list"')
print(f'Starting list is: {my_list}')
print(f'Resulting list is: {new_list}')


# ----------------------------------------------------------2----------------------------------------------------------


for i in range(1, len(my_list), 1):
    if my_list[i] > my_list[i - 1]:
        new_list_1.append(my_list[i])
print('\nSecond solution')
print(f'Resulting list is: {new_list_1}')


# ----------------------------------------------------------3-----------------------------------------------------------


def is_more_num(my_list):
    new_list_2 = [my_list[num_el] for num_el in range(1, len(my_list)) if my_list[num_el] > my_list[(num_el - 1)]]
    return print(f'Resulting list is: {new_list_2}')


print('\nThird solution')
print(f'Starting list new_list_3: {new_list_3}')
is_more_num(new_list_3)

