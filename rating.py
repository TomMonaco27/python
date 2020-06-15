# Lesson 2 Task 5
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

stop_program = ''
my_list = [7, 5, 3, 3, 3, 3, 2, 2, 1]
print(my_list)

while stop_program != 'y':
    number = int(input('Введите натуральное число: '))
    count_number = my_list.count(number)
    if count_number == 0:
        my_list.insert(0, number)
    elif count_number == 1:
        first_found_ones = my_list.index(number)
        my_list.insert(first_found_ones + 1, number)
    elif count_number > 1:
        first_found = my_list.index(number)
        print(f'first_found {first_found}')
        for el in range(count_number - 1):
            last_found = my_list.index(number, first_found + 1)
            first_found = last_found
            print( f'last_found {last_found}')
            my_list.insert(last_found + 1, number)

    print(my_list)
    stop_program = input('Продолжаем ввод? Нажмите любая клавиша для продолжения или "y" чтобы закончить работу программы: ')
