# lesson 1 Task 3
# Программа "Sum Number"
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

print('Программа "Sum number"')
number = int(input('Введите целое число: '))
sum_number = number + number*10+number + number*100+number*10+number
print(f'Сумма {number}+{number}{number}+{number}{number}{number} = {sum_number}')