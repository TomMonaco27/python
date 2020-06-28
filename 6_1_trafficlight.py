"""
lesson-6 Task 1
Program "TrafficLight"
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""


import time
from itertools import cycle, islice


class TrafficLight:
    __color = ['red', 'yellow', 'green', 'yellow']

    def running(self, count_number):
        try:
            if count_number.isdigit():
                iter = cycle(TrafficLight.__color)
                for el in islice(iter, int(count_number)):
                    if el == 'red':
                        print(f'\033[31m{el}')
                        time.sleep(7)
                    elif el == 'yellow':
                        print(f'\033[33m{el}')
                        time.sleep(2)
                    else:
                        print(f'\033[32m{el}')
                        time.sleep(7)
            else:
                return print('Error! Your enter not digits!')
        except:
            print('Error in method running() class TrafficLight! Something wrong, but don\'t worry, be happy.'
                  ' Maybe next time, buy yourself a ice cream :)')
        finally:
            print('\033[30mEnd the program.')


name_program = "TrafficLight"
print('Program "', end='')
color = ['\033[31m', '\033[33m', '\033[32m']
iter = cycle(color)
for i in range(len(name_program)):
    for el in islice(iter, 1):
        print(f'{el} {name_program[i]}', end='')
print('\033[30m"\n', end= '')
my_traffic_light = TrafficLight()
my_traffic_light.running(input("How many traffic light cycles do you want: "))
