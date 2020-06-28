"""
lesson-6 Task 4
Program "Type of cars"
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


from random import randint
from time import sleep


class Car:
    color_car = {'чёрный': '\033[30m', 'красный': '\033[31m', 'зелёный': '\033[32m', 'жёлтый': '\033[33m',
               'синий': '\033[34m', 'фиолетовый': '\033[35m', 'бирюзовый': '\033[36m',
                 'black': '\033[30m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m',
                'blue': '\033[34m', 'purple': '\033[35m', 'turquoise': '\033[36m'}

    direction_list = ['left', 'right', 'straight ahead']

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        self.show_speed()

    def go(self):
        return print(f'car {self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]} is going.')

    def stop(self):
        return print(f'car {self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]} is stop.')

    def turn(self, direction):
        return print(f'car {self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]} is going to {direction}.')

    def show_speed(self):
        return print(f'speed of car {self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]} is {self.speed} ')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            if_high_speed_info = f'speed {self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]} to high!' \
                                 f' Above than 60! Now speed is {self.speed}'
            return print(if_high_speed_info)
        if_normal_speed_info = f'speed {self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]} is {self.speed} '
        return print(if_normal_speed_info)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            if_high_speed_info = f'speed {self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]} to high! ' \
                                 f'Above than 60! Now speed is {self.speed}'
            return print(if_high_speed_info)
        if_normal_speed_info = f'speed {self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]} is {self.speed} '
        return print(if_normal_speed_info)


class PoliceCar(Car):
    def turn(self):
        return print(f'car \033[6m{self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]} is going to'
                     f' {self.direction_list[randint(0, 2)]}.')

    def go(self):
        for i in range(50):
            print(f'\033[31m{self.name} \033[30mis going', end='')
            sleep(.1)
            print('\r', end='')
            print(f'\033[34m{self.name} \033[30mis going', end='')
            sleep(.1)
            print('\r', end='')
        return print(f'\033[34m{self.name} \033[30mis going')


print('Program "Type of cars"')
# town_car
town_car = TownCar('Town car', 50, 'purple', False)
town_car = TownCar('Town car', 80, 'зелёный', False)
# work_car
work_car = WorkCar('Work car', 130, 'жёлтый', False)
work_car = WorkCar('Work car', 30, 'синий', False)
work_car.go()
work_car.turn('left')
# police_car
car_police = PoliceCar('Police car', 110, 'красный', True)
print(f'name car is: {car_police.name}')
car_police.show_speed()
# sport_car
sport_car = SportCar('Sport car', 300, 'turquoise', False)
# police_car мигает
car_police.turn()
car_police = PoliceCar('Patrol police car', 110, 'красный', True)
car_police.go()
