"""
Lesson 3 Task 1.
Program "Division Function"
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def div_func(numerator, denominator):
    """
     Выводит на экран частное от деления,
     или возвращает строку с сообщением об ошибке, в случае если делитель равен 0

     Позиционные аргументы:
     numerator -- делимое
     denominator -- делитель

     пример:
     10 / 1 = 10
     """
    if denominator == 0:
        print('Error! Division by zero!')
        return 'Error! Division by zero!'
    division = numerator / denominator
    print(f'Division: {numerator} / {denominator} = {division:.04}')


print('Program "Division Function"')
div_func(numerator=float(input('Enter numerator: ')), denominator=float(input('Enter denominator: ')))


# -----------------------------------------------------2-----------------------------------------------------------------
# рассмотрен вариант ловли ошибки при делении на ноль,
# но без позиционных аргументов, для тренировки ввода данных внутри функции


def div_func_2():

    numerator_2 = float(input('Enter numerator: '))
    denominator_2 = float(input('Enter denominator: '))

    try:
        division_2 = numerator_2 / denominator_2
    except ZeroDivisionError:
        print('Error! Division by zero!')
        return 'Enter a nonzero denominator next time)'
    finally:
        print('End the program.')
    return f'Division: {numerator_2} / {denominator_2} = {division_2:.04}'


print('Program "Division Function"')
print(div_func_2())


# -----------------------------------------------------3-----------------------------------------------------------------


def input_numbers():
    global numerator_3, denominator_3
    numerator_3 = float(input('Enter numerator: '))
    denominator_3 = float(input('Enter denominator: '))
    if denominator_3 == 0:
        print('Error! Denominator is zero! Re-enter denominator')
        return input_numbers()
    return numerator_3, denominator_3


def div_func_3(numerator_3, denominator_3):
    division_3 = numerator_3 / denominator_3
    print(f'Division: {numerator_3} / {denominator_3} = {division_3:.04}')


print('Program "Division Function"')
input_numbers()
div_func_3(numerator_3, denominator_3)
