"""
lesson-6 Task 3
Program "Get total income of worker"
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        self.separator = ' '


class Position(Worker):

    def get_full_name(self):
        self.full_name = self.name + self.separator + self.surname
        return print(f'Full name is : {self.full_name}')

    def get_total_income(self):
        try:
            self.isdigit_wage = float(self._income['wage'])
            self.isdigit_bonus = float(self._income['bonus'])
            self.sum = self.isdigit_wage + self.isdigit_bonus
            return print(f'Sallary of {self.full_name} is {self.sum:.4f}')
        except ValueError:
            print('\033[31mError get_total_income()! Please enter a digits!\033[30m')
        except:
            print('\033[31mError get_total_income()\033[30m')


print('Program "Get total income of worker"')
director = Position('Ivan', 'Ivanov', 'director',100, 100.45567)
director.get_full_name()
director.get_total_income()
print(f'{director.full_name} position is {director.position}')
teacher = Position('Eugene', 'Ivanov', 'teacher',600, 100.45567)
teacher.get_full_name()
teacher.get_total_income()