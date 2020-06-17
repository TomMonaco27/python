"""
Lesson 3 Task 2.
Program "Personal information"
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(name, surname, year_of_birth, current_city, email, phone):
    print(f'{name}, {surname}, {year_of_birth}, {current_city}, {email}, {phone}')


print('Program "Personal information"')
user_data(surname=input('Enter your surname: '), name=input('Enter your name: '), year_of_birth=input('Enter your year of birth: '),
          current_city=input('Enter your current_city: '), email=input('Enter your email: '), phone=input('Enter your phone: '))
