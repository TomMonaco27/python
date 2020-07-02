"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    const_coat_6_5 = 6.5
    const_coat_0_5 = 0.5
    const_suit_2 = 2
    const_suit_0_3 = 0.3

    def __init__(self, size, height):
        try:
            self.size = size
            self.height = height
        except:
            print('Error __init__ Clothes')

    @abstractmethod
    def consumption_fabric(self, size, height):
        pass

class Coat(Clothes):
    def __init__(self, size=1):
        try:
            self.size = size
        except:
            print('Error! __init__')

    @property
    def size(self):
        try:
            return self.__size
        except:
            print('Error! size()')

    @size.setter
    def size(self, size):
        try:
            if not isinstance(size, (int, float)):
                print('Error! you enter not number')
            if size < 46:
                self.__size = 44  # устанавливаем размер xs
            elif 46 <= size <= 48:
                self.__size = 48  # устанавливаем размер s
            elif 48 < size <= 50:
                self.__size = 50  # устанавливаем размер m
            else:
                self.__size = 52  # размер l и выше( к сожалению, оверсайза нет, ищите другой магазин...
        except ValueError:
            print('Error! size.setter')

    def consumption_fabric(self):
        try:
            self.consumption_fabric = self.size / self.const_coat_6_5 + self.const_coat_0_5
            return self.consumption_fabric
        except:
            print('Error in consumption_fabric() class Coat')

    def __str__(self):
        try:
            return f'Сonsuption fabric on Coat need on your size {str(self.size)} is {self.consumption_fabric:.2f} '
        except:
            print('Error __str__ class Coat')


class Suit(Clothes):
    def __init__(self, height=1):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        try:
            if not isinstance(height, (int, float)):
                print('Error! you enter not number')
            if height < 150:
                self.__height = 150  # устанавливаем рост 150
            elif 150 <= height <= 165:
                self.__height = 165  # устанавливаем рост 165
            elif 165 < height <= 180:
                self.__height = 180  # устанавливаем рост 180
            else:
                self.__height = 200  # устанавливаем рост 200
        except ValueError:
            print('Error! height.setter')

    def consumption_fabric(self):
        try:
            self.consumption_fabric = self.height / self.const_suit_2 + self.const_suit_0_3
        except:
            print('Error in consumption_fabric() class Suit')
        return self.consumption_fabric

    def __str__(self):
        try:
            return f'Consuption fabric to your Suit need for your hight {str(self.height)} is : {self.consumption_fabric:.1f}'
        except:
            print('Error __str__ class Suit')


new_coat = Coat(1)
new_coat.consumption_fabric()
print(new_coat)
new_coat = Coat(47)
new_coat.consumption_fabric()
print(new_coat)
new_coat = Coat(49)
new_coat.consumption_fabric()
print(new_coat)
new_coat = Coat(55)
new_coat.consumption_fabric()
print(new_coat)

new_suit = Suit(149)
new_suit.consumption_fabric()
print(new_suit)
new_suit = Suit(155)
new_suit.consumption_fabric()
print(new_suit)
new_suit = Suit(180)
new_suit.consumption_fabric()
print(new_suit)
new_suit = Suit(200)
new_suit.consumption_fabric()
print(new_suit)
