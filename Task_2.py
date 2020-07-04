"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
"""


class MyDivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


print('Program "MyDivisionByZero"')
dividend = input('Enter dividend: ')
divider = input('Enter divider: ')


try:
    result = int(dividend) / int(divider)
    if int(divider) == 0:
        raise MyDivisionByZero('My error division by zero')


except MyDivisionByZero as div_zero_err:
    print(div_zero_err)
except ValueError:
    print('Value error!')
#except ZeroDivisionError:
#    raise MyDivisionByZero('My error division by zero')
else:
    print(f'Result: {result}')
finally:
    print('End the program.')



