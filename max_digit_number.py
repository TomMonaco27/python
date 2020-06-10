# lesson 1 Task 4
# Программа "Maximum digit in number"
# Пользователь вводит целое положительное число. Найдите самую
# большую цифру в числе. Для решения используйте цикл while и арифметические операции. 612345   61

max_digit = 0
print('Программа "Maximum digit in number"')
positive_int_num = int(input('Введите положительное целое число: '))


while positive_int_num != 0:
    if max_digit == 9:
        print(f'max_digit = {max_digit}')
        break

    digit = positive_int_num % 10

    if digit > max_digit:
        max_digit = digit
    positive_int_num = positive_int_num // 10

print(f'Самая большая цифра в числе = {max_digit}')
