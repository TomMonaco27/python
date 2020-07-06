"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""
class StorehouseOfficeEquipment:
    storehouse_list = []
    storehouse_dict = {}
#    def __init__(self, name_office_equipment):
#        self.name_office_equipment = name_office_equipment

    def __init__(self):
        pass



    def goods_reception(*list):
        StorehouseOfficeEquipment.storehouse_list.append(*list)
#        self.storehouse_list.append(*list)
#        self.storehouse_list = number_model, serial_number
#        self.storehouse_dict[self.name_office_equipment] = self.storehouse_list
#        self.storehouse.append(self.storehouse_dict[name_office_equipment])
#        print(f'{self.storehouse_dict}')
#        print(f'Save in base: {self.storehouse_list}')
        print(f'Save in base: {StorehouseOfficeEquipment.storehouse_list}')
#        print(f'name_office_equipment {name_office_equipment} , quantity {quantity}')

    def departure_goods(self, quantity, department_number):
        pass

    def look_storehouse(self):
        print(f'Storehouse: {self.storehouse}')

class OfficeEquipment:

    def __init__(self, name_office_equipment, serial_number, number_model):
        self.name_office_equipment = name_office_equipment
        self.serial_number = serial_number
        self.number_model = number_model


class Printer(OfficeEquipment):
    printer_dict = {}
    printer_list = [0, 0, 0, 0]
    printer_list_temp = []
    list_1 = []
    def __init__(self, name_office_equipment, serial_number, number_model, type_printer):
        super().__init__(name_office_equipment, serial_number, number_model)
        self.type_printer = type_printer # laser, jet, matrix
#        self.printer_dict['name'] = self.name_office_equipment
#        self.printer_dict['serial_number'] = self.serial_number
#        self.printer_dict['number_model'] = self.number_model
#        self.printer_dict['type_printer'] = self.type_printer
#        self.printer_list.append(name_office_equipment)
#        self.printer_list.append(serial_number)
#        self.printer_list.append(number_model)
#        self.printer_list.append(type_printer)
        self.printer_list[0] = self.name_office_equipment
        self.printer_list[1] = self.serial_number
        self.printer_list[2] = self.number_model
        self.printer_list[3] = self.type_printer

#    def add_printer(self, *list):
#       self.list = *list
#       for el in self.list:
#           StorehouseOfficeEquipment().goods_reception(el)
#            self.printer_list[0] = self.name_office_equipment
#            self.printer_list[1] = self.serial_number
#            self.printer_list[2] = self.number_model
#            self.printer_list[3] = self.type_printer
        return self.printer_list

    def add_printer(self):
        StorehouseOfficeEquipment().goods_reception(self.printer_list)


    def __str__(self):
        print('Class Printer')
        print(f'printer_dict: {self.printer_dict}')
        print(f'printer_list: {self.printer_list}')
        return f'Name of office equipment: {self.name_office_equipment}, serial number: {self.serial_number},' \
               f' number model: {self.number_model} type printer: {self.type_printer}'

print('Start program')
printer_1 = Printer('printer', 111, '13bf', 'laser')
#printer_1.add_printer()
#order_1 = StorehouseOfficeEquipment()
#StorehouseOfficeEquipment.goods_reception(printer_1.add_printer())
#print('Создан объект printer_1')
#print(printer_1.add_printer())
StorehouseOfficeEquipment.goods_reception(printer_1.add_printer(printer_1))
#
printer_2 = Printer('printer', 222, '122bf', 'matrix')
StorehouseOfficeEquipment.goods_reception(printer_2.add_printer(printer_2))
#printer_2.add_printer()
#order_2 = StorehouseOfficeEquipment()
#StorehouseOfficeEquipment.goods_reception(printer_2.add_printer())
#StorehouseOfficeEquipment.goods_reception(printer_2.add_printer())
#print(printer_2)
#order_2 = StorehouseOfficeEquipment('printer')
#StorehouseOfficeEquipment.goods_reception(order_2, printer_2.add_printer())
printer_3 = Printer('scaner', 333, '33bf', 'nomatrix')
#printer_2.add_printer()

order_3 = StorehouseOfficeEquipment()
#printer_1.add_printer(printer_1)


#StorehouseOfficeEquipment.look_storehouse(order_1)
