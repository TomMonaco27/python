"""
lesson 8 Task 1
Program "Check date with using classmethod and staticmethod"
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_extraction(cls, date):
        day, month, year = map(int, date.split('-'))
        print(f'Day is: {day}, month is: {month}, year is: {year}')
        data_list = [day, month, year]
        return data_list

    @staticmethod
    def valid_date(date_list):
        if 1 > date_list[0]:
            print('Day is wrong')
        elif date_list[0] > 31:
            print('Day is wrong')
        if 1 > date_list[1]:
            print('Month is wrong')
        elif date_list[1] > 12:
            print('Month is wrong')
        if 1 > date_list[2]:
            print('Year is wrong')
        elif date_list[2] > 2099:
            print('Year is wrong')


print('Program "Class data with use classmethod, staticmethod"')
my_time = input('Please , enter data in format DD-MM-YY: ')
#my_time = '3-1-2'
Data.valid_date(Data.date_extraction(my_time))
print('End of the program.')


