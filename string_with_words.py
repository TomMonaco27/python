# Lesson 2 Task 4
# Программа "String with words"
# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
# необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

print('Программа "String with words"')
input_string = input('Введите строку из нескольких слов, разделённых пробелами: ')
list = input_string.split(' ')

for index, element in enumerate(list, 1):
        print(f'{index}.{element[:10:]}')
