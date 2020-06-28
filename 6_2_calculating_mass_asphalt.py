"""
lesson-6 Task 2
Program "Calculating mass of asphalt"
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculating_mass_asphalt(self):
        try:
            self.mass = self._length * self._width * 25 * 0.05
            return print(f'asphalt mass = {self.mass / 1000} ton')
        except ZeroDivisionError:
            print('Error! Divizion by Zero!')
        except:
            print('Error in method calculating_mass_asphalt() class Road! Something wrong, but don\'t worry, be happy.'
                  ' Maybe next time, buy yourself a ice cream :)')


print('Program "Calculating mass of asphalt"')
avtodor_crimea = Road(20, 5000)
avtodor_crimea.calculating_mass_asphalt()