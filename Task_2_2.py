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
#    consumption_fabric = 0
    const_coat_6_5 = 6.5
    const_coat_0_5 = 0.5
    const_suit_2 = 2
    const_suit_0_3 = 0.3

    @abstractmethod
    def consumption_fabric(self):
        pass

#    def __str__(self):
#        return f'need {self.consumption_fabric}'


class Coat(Clothes):
    def __init__(self, size=1):
        self.size = size

    def consumption_fabric(self):
        self.consumption_fabric = self.size / self.const_coat_6_5 + self.const_coat_0_5
        return self.consumption_fabric

    def __str__(self):
        return f'Coat need consuption_fabric: {self.consumption_fabric:.4f}'


class Suit(Clothes):
    def __init__(self, height=1):
        self.height = height

    def consumption_fabric(self):
        self.consumption_fabric = self.height / self.const_suit_2 + self.const_suit_0_3
        return self.consumption_fabric

    def __str__(self):
        return f'Suit need consuption_fabric: {self.consumption_fabric:.4f}'


new_coat = Coat(11)

new_coat.consumption_fabric()
print(new_coat)
new_suit = Suit(11)
new_suit.consumption_fabric()
print(new_suit)
