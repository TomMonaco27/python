""" Lesson 4 Task 6
Program "scripts_with_count_cycle"
Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
#Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""


# ----------------------------а)итератор, генерирующий целые числа, начиная с указанного--------------------------------
from sys import argv
from itertools import count, cycle, islice

script_name, start_number = argv

print('Program "scripts with count cycle"')
print('itertools.count() c выходом по break:')
for el in count(int(start_number)):
    if el > 10:         # выход с break
        break
    else:
        print(el)

# -----------------------------------------------------1---------------------------------------------------------------


print('\nОграничение itertools.count() без break, использование islice:')
for el in islice(count(int(start_number)), 8):
    print(el)


# -------------------------------------------------2-------------------------------------------------------------------


print('\nОграничение itertools.count() без break, использование function:')


def count_func(start_number):
    try:
        for el in count(int(start_number)):
            if el == 11:
                return print('Stop count, because find 10:)')
            print(el)
    except ValueError:
        return print('Imput value is wrong...')
    finally:
        print('End work with itertools.count\n')


count_func(start_number)


# -------------------б) итератор, повторяющий элементы некоторого списка, определенного заранее-------------------------

print('\nОграничение itertools.cycle() c помощью islice:')
my_list = [1, 2, 3, 4]
iter = cycle(my_list)
for el in islice(iter, int(start_number)):
    print(el)


