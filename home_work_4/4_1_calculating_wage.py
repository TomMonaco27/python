"""
Lesson 4 Task 1
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрам
"""


import sys


def wage(output_per_hour, rate_per_hour, bonus):
    return (int(output_per_hour) * int(rate_per_hour)) + int(bonus)


script_name, output_per_hour, rate_per_hour, bonus = sys.argv

print(f'Program name is: {script_name} ')
print(f'Output per hour a employee: {output_per_hour} rubles')
print(f'Rate per hour a emloyee: {rate_per_hour} rubles')
print(f'Bonus of a employee: {bonus} rubles')
print(f'Wage of a employee: {wage(output_per_hour, rate_per_hour, bonus)} rubles')
