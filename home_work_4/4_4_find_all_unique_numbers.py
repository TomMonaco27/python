"""
Lesson 4 Task 4
Program "find all unique numbers in the list"
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""


starting_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print("Program find all unique numbers in the list")
print(f'Starting list is: {starting_list}')
new_list = [el for el in starting_list if starting_list.count(el) == 1]
print(f'New list with only unique numbers: {new_list}')
