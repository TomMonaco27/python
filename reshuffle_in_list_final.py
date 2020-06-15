# Lesson 2 Task 2
# Программа "Reshuffle in list"
# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

temp_element = 0
list = []

print('Программа "Reshuffle in list"')
str_input = input('Введите элементы для добавления в список, через пробел: ')
list = str_input.split(' ')  # преобразование str в list
len_list = len(list)
for element in range(0, len_list, 2):
    if element + 1 == len_list:  # если нечетное число элементов - конец перестановкам - выход
        break
    temp_element = list[element + 1]
    list[element + 1] = list[element]
    list[element] = temp_element

print(f'Список после перестановок:\n{list}')


