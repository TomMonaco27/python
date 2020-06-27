"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
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
#    name = 'Ivanov'
#    surname = 'Surname'
#    position = 'middle'
#    _income = 10 #{"wage": 10, "bonus": 10}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        self.full_name = self.name + self.separator + self.surname
        return print(f'Full name is : {self.full_name}')

    def get_total_income(self):
        try:
            self.isdigit_wage = str(self._income['wage']).isdigit
            self.isdigit_bonus = str(self._income['bonus']).isdigit
#            print(self.isdigit_bonus)
#            print(self.isdigit_wage)
            while str(self._income['wage']).isdigit and str(self._income['bonus']).isdigit:
                self.sum = self._income['wage'] + self._income['bonus']
                return print(self.sum, type(self.isdigit_bonus), self.isdigit_wage)
        except:
            print('Error get_total_income()')

director = Position('Ivan', 'Ivanov', 'director', 10, 10)
director.get_full_name()
director.get_total_income()