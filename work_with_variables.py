# Lesson 1 Task 1
# program "work_with_variables"
# Поработайте с переменными, создайте несколько, выведите на экран, запросите у
# пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

var_int = 123
var_float = 123.123
var_complex = complex(1, 2)
var_str_digits = "123"
var_str = "one two tree"
var_none = None
var_bool = True


print('Программа "Work with variables"')
print(f'var_int = {var_int}')
print(f'var_float = {var_float}')
print(f'var_complex = {var_complex}')
print(f'var_str_digits = {var_str_digits}')
print(f'var_str = {var_str}')
print(f'var_none = {var_none}')
print(f'var_bool = {var_bool}')



var_int = int(input('\nВведите десятичное число: '))
var_float = float(input('Введите вещественное число: '))
var_complex = complex(input('Введите комплексное число: '))
var_str = input('Введите строку: ')

print(f'\nVar_int = {var_int}')
print(f'Var_float = {var_float}')
print(f'Var_complex = {var_complex}')
print(f'Var_str = {var_str}')