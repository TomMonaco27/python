class StorehouseOfficeEquipment:
    #storehouse_list = []
    def __init__(self):
        self.storehouse_list = []

    def to_take(self, *info):
#        self.info = list(info)
        self.storehouse_list.append(*info)
        print(f'{self.storehouse_list}')
#        return f'{self.storehouse_list[0]}'
class OfficeEquipment:  #Pupil(person)
   pass

class Printer(OfficeEquipment):  #subject
    def __init__(self, *data_printer):
        self.printer_list = []
#        self.data_printer = list(data_printer)
        print(self.printer_list)

    def to_take_printer(self, *info):
#        StorehouseOfficeEquipment.to_take(*info)
        self.printer_list.append(*info)
        print(f'{self.printer_list}')
        return self.printer_list

list_1 = [1, 1]
list_2 = [2, 2]
printer_1 = Printer('printer', 'model111')
printer_1.to_take_printer(printer_1)
order_1 = StorehouseOfficeEquipment()
order_1.to_take(printer_1.to_take_printer(printer_1))





