"""
lesson 8 Task 3
Program "My NotDigitError"
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и
отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""


class NotDigitError(Exception):
    def __init__(self, text):
        self.txt = text


input_text = 'n'
final_list = []
print('Program "My NotDigitError"')

while input_text != 'q':
    try:
        input_text = input('Input numbers to write to list. To "Quit" please enter - q: ')
        if input_text == 'q':
            break
        if not input_text.isdigit():
            raise NotDigitError('You enter not digits!')
        final_list.append(int(input_text))
        continue
    except NotDigitError as MyErr:
        print(MyErr)
        continue


print(f'Your final list is: {final_list}')
print('End of the program.')