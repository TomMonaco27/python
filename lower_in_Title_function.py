"""
Lesson 3 Task 6.
Program "lower_in_Title_function"
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В
программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем
регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
использовать написанную ранее функцию int_func().
"""


def int_func(lower_str):
    return lower_str.title()


new_list = []

print('Program "lower_in_Title_function"')
print(f'Word in title case: {int_func(lower_str=input("Enter a word in lower case: "))}')
str = input('Enter a string with lower case words through the space bar: ').split()
for el in str:
    new_list.append(int_func(el))

new_str = ' '.join(new_list)  # преобразование списка в строку с разделителем пробел
print(f'New string wiht title words: {new_str}')


# ----------------------------------------------------------------2------------------------------------------------------


def int_func(lower_str):
    while lower_str != lower_str.lower():
        lower_str = input('Enter only lower text: ')
    return lower_str.title()


new_list = []

print('Program "lower_in_Title_function"')
print(f'Word in title case: {int_func(lower_str=input("Enter a word in lower case: "))}')
str = input('Enter a string with lower case words through the space bar: ')
while str.replace(' ', '').lower() != str.replace(' ', ''):
    print('Wrong! Re-enter again')
    str = input('Enter a string with lower case words through the space bar: ')
while not str.replace(' ', '').islower():
    print('Wrong! Re-enter again')
    str = input('Enter a string with lower case words through the space bar: ')
list = str.split()
for el in list:
    new_list.append(int_func(el))

new_str = ' '.join(new_list)  # преобразование списка в строку с разделителем пробел
print(f'New string with Title words: {new_str}')
