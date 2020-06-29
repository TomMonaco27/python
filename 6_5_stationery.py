"""
lesson-6 Task 5
Program "Stationery"
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery():
    _title = 'канцелярская принадлежность'
    def draw(self):
        return print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        return print(f'Запуск отрисовки {self._title}: ручка')


class Pencil(Stationery):
    def draw(self):
        return print(f'Запуск отрисовки {self._title}: карандаш')


class Handle(Stationery):
    def draw(self):
        return print(f'Запуск отрисовки {self._title}: маркер')


print('Program "Stationery"')
print(Stationery.__dict__) # узнаем какие атрибуты и методы есть у класса, что в дальнейшем их вызывать
print(Pen.__dict__) # узнаем какие атрибуты и методы есть у класса
print(Pencil.__dict__)
print(Handle.__dict__)
print(getattr(Stationery, '_title')) # используем getattr(class, 'name_attribute') для доступа к значениям
print(getattr(Pen, 'title', 'no such attribute')) # используем getattr(class, 'name_attribute', if_not_find_attr_value)
                                                # для доступа к значениям, в случае отсутствия элемента выводим сообщение
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
print(pencil._title)
print(Stationery._title)
# создадим новый, отсутствующий атрибут в классе Stationery, простым добавлением после точки.
Stationery.price = 100
print(Stationery.price)
# поменяем значение атрибута в классе Stationery на список цен, т.к. у нас три канцелярские принадлежности:)
Stationery.price = [100, 200, 300]
print(Stationery.price)
# получим доступ к родительскому защищенному атрибуту и меняем первую букву на заглавную
pencil._Stationery_title = 'Канцелярская принадлежность'
print(pencil._Stationery_title)
# используем встроеную функцию setattr(class, name_attribute, value_attribute) для установления значения новому атрибуту
setattr(Stationery, 'name_shop', 'Comus')
print(Stationery.name_shop)
print(Stationery.__dict__)
# удаляем атрибут 'name_shop' c помощью del
del Stationery.name_shop
print(Stationery.__dict__)
# удаляем атрибут 'name_shop' c помощью delattr
delattr(Stationery, 'price')
print(Stationery.__dict__)
# локальные, глобальные переменные
# посмотрим атрибуты дочернего класса Pen() и создадим локальный атрибут в классе Pen()
print(pen.__dict__)
pen.weight = 10
print(pen.__dict__)
# создадим локальный атрибут _title в классе Pen()
pen._title = "канцелярская принадлежность номер 1: "
# удаляем локальную переменную _title в классе Pen()
del pen._title
# смотрим глобальную переменную _title из класса Stationery(), т.к. локальную мы удалили
print(pen._title)
