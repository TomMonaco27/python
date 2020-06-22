"""
Lesson 4 Task 3
'Program "Find multiple numbers of 20 and 21 in the list"
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""

print('Program "Find multiple numbers of 20 and 21 in the list"')
print(f'Starting list: {[el for el in range(20, 240)]}')
new_list_2 = [el for el in range(20, 240) if el % 21 == 0 or el % 20 == 0]
print(f'New list with multiple numbers of 20 and 21: {new_list_2}')
