import re
import os # для удаления созданной выгрузки
import sys # узнаем где стоит интепретатор python
import shutil # Обеспечиваем бэк ап



class StorehouseOfficeEquipment:
    # storehouse_list = []
    def __init__(self):
        self.storehouse_list = []


    def take_to_warehouse(self, *info):
#        self.info = list(info)
        self.storehouse_list.append(*info)
        print(f'Add {self.storehouse_list[-1]}')
#        print(f'Storehouse: {self.storehouse_list}')

    def take_from_warehouse(self, number_model):
        for list in self.storehouse_list:
            for el in list:
                print(el)
#        result = re.search(number_model, self.storehouse_list)
#        print(result)

    def find_in_warehouse(self, name_office_equipment, number_model):
        try:
            for el in range(len(self.storehouse_list)):
                if self.storehouse_list[el][0] == name_office_equipment and self.storehouse_list[el][1] == number_model:
                    print(self.storehouse_list[el][1], self.storehouse_list[el][1] == number_model)
                    print(f'Find item {self.storehouse_list[el][0]}, model {self.storehouse_list[el][1]}: {self.storehouse_list[el]}')
        except:
            print('Error find_in_warehouse() class "StorehouseOfficeEquipment"')

    def sum_items_warehouse(self, name_office_equipment):
        try:
            self.sum_items = 0
            for el in range(len(self.storehouse_list)):
                if self.storehouse_list[el][0] == name_office_equipment:
                    self.sum_items += 1
            print(f'We have at Storehouse {name_office_equipment}: {self.sum_items}')
        except:
            print('Error sum_items_warehouse() class "StorehouseOfficeEquipment"')
#        return f'{self.storehouse_list[0]}'

    def save_to_file(self, name_file_write):
        try:
            total = 0
            total_printers = 0
            total_scanners = 0
            total_copiers = 0
            with open(name_file_write, 'w', encoding='utf-8') as f_obj:
                for key, value in enumerate(range(len(self.storehouse_list)), 1):
                    f_obj.write(f'{key}. {self.storehouse_list[value]}\n')
                    if self.storehouse_list[value][0] == 'printer':
                        total_printers += 1
                    if self.storehouse_list[value][0] == 'scanner':
                        total_scanners += 1
                    if self.storehouse_list[value][0] == 'copier':
                        total_copiers += 1
                total = key
                print(f'Total: {total},\tprinters: {total_printers},\tscanners: {total_scanners},\tcopiers: {total_copiers}', file=f_obj)
                print(f'Writing to file: {name_file_write} ok')
        except IOError:
            print('Error save_to_file() class "StorehouseOfficeEquipment"a')
        except:
            print('Error save_to_file() class "StorehouseOfficeEquipment"')

    def delete_file(self, name_file_write):
        try:
            os.remove(name_file_write)
        except FileNotFoundError:
            print('Error delete_file() class "StorehouseOfficeEquipment". File not found')
        except:
            print('Error delete_file() class "StorehouseOfficeEquipment"')

    def look_all_warehouse(self):
        try:
            print(f'Warehouse: {self.storehouse_list}')
        except:
            print('Error look_warehouse() class "StorehouseOfficeEquipment"')

    def backup_data(self, name_file_read, name_file_write_backup):
        with open(name_file_read, 'r', encoding='utf-8') as f_obj_1:
            with open(name_file_write_backup, 'w', encoding='utf-8') as f_obj_2:
                shutil.copyfileobj(f_obj_1, f_obj_2)



class OfficeEquipment:  # Pupil(person)
    def __init__(self, name_office_equipment):
        self.name_office_equipment = name_office_equipment


class Printer(OfficeEquipment):  # subject
    def __init__(self, name_office_equipment, number_model, serial_number):
        super().__init__(name_office_equipment)
        self.printer_list = []
#        self.data_printer = list(data)
        self.data_printer = [name_office_equipment, number_model, serial_number]

    #        print(self.printer_list)

    def add_printer(self):
#        self.printer_list = self.data_printer
#        print(f'Add list: {self.printer_list}')
        return self.data_printer


order_1 = StorehouseOfficeEquipment()

printer_1 = Printer('printer', 'laserJet1', '1112')
order_1.take_to_warehouse(printer_1.add_printer())
order_1.take_from_warehouse('1')
printer_1 = Printer('scanner', 'Scan2', '1113')
order_1.take_to_warehouse(printer_1.add_printer())
printer_1 = Printer('printer', 'laserJet2', '1114')
order_1.take_to_warehouse(printer_1.add_printer())


order_1.find_in_warehouse('printer', 'laserJet1')
order_1.sum_items_warehouse('printer')
order_1.sum_items_warehouse('scanner')
order_1.save_to_file('warehouse.txt')
order_1.backup_data('warehouse.txt', 'backup_warehouse.txt')
order_1.delete_file('warehouse.txt')
order_1.look_all_warehouse()
order_1.save_to_file('warehouse_1.txt')



print('\nTechnical info')
# для отладки работы программы в дальнейщем, программистам может быстро понадобится вся информация о систем где и как работает программа
print(f'Interpretator python here: {sys.executable}')
print(f'System: {sys.platform}')

'''
print('Program "Storehouse Office Equipment"')
order_1 = StorehouseOfficeEquipment()
menu_input = input('1. Add item\n2. Find item\nExit press "q"\nEnter menu: ')

while menu_input != 'q':
    if menu_input == '1':
        print('\nAdd office equipment')
        name_office_equipment = input('Please, enter name_office_equipment: ')
        number_model = input('Please, number_model: ')
        printer_1 = Printer(name_office_equipment, number_model)

        order_1.take_to_warehouse(printer_1.add_printer())
        order_1.take_from_warehouse(number_model)
        menu_input = input('Exit press q: ')
    if menu_input == '2':
        print('\nFind office equipment:')
        name_office_equipment = input('Please, enter name_office_equipment: ')
        number_model = input('Please, number_model: ')
        order_1.find_in_warehouse(name_office_equipment, number_model)
        
#order_1.take_to_warehouse(printer_2.add_printer())
print('End the program.')
'''