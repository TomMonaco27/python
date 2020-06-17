"""
Lesson 3 Task 5.
Program "Sum up to special character"
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

sum_digit = 0


def check_input():
    global sum_digit
    str_digit = input('Enter digits separated by space: ').split()
    for i, el in enumerate(str_digit):
        if str_digit[i] == chr(97):
            print(f'Sum of entered digits is {sum_digit}')
            return print('End of the program.')
        str_digit[i] = int(el)
        sum_digit += str_digit[i]
    print(f'Sum of entered digits is {sum_digit}')
    check_input()


def main():
    print('Program "Sum up to special character"')
    print('Stop enter and exit - special character: "a"')
    check_input()


if __name__ == '__main__':
    main()
