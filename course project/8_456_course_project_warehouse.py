
import os  # для удаления созданной выгрузки
import sys  # узнаем где стоит интепретатор python
import shutil  # Обеспечиваем бэк ап
from time import sleep  # задержка при не пеправильном вводе пароля
import uuid  # uuid используется для генерации случайного числа
import hashlib


class WarehouseOfficeEquipment:
    def __init__(self, warehouse_manager):
        try:
            self.warehouse_list = []
            self.warehouse_manager = warehouse_manager
        except:
            print(f'Error __init__ class "WarehouseOfficeEquipment"')

    # добавить на склад
    def take_to_warehouse(self, *info):
        try:
            self.warehouse_list.append(*info)
            print(f'\nAdd: \033[34m{self.warehouse_list[-1]}\033[0m')
        except:
            print('Error take_to_warehouse() class "WarehouseOfficeEquipment"')

    # удалить со склада
    def delete_from_warehouse(self, number_model):
        try:
            count_elements = 0
            for list in self.warehouse_list:
                count_elements += 1
                for el in list:
                    if el == number_model:
                        print(f'\033[31mDelete item:\033[30m {list}')
                        self.warehouse_list.pop(count_elements - 1)
        except:
            print('Error delete_from_warehouse() class "WarehouseOfficeEquipment"')

    # найти на складе по номеру модели
    def find_in_warehouse(self, name_office_equipment, number_model):
        try:
            find_item = 0
            for el in range(len(self.warehouse_list)):
                if self.warehouse_list[el][0] == name_office_equipment and self.warehouse_list[el][1] == number_model:
                    print(self.warehouse_list[el][1], self.warehouse_list[el][1] == number_model)
                    print(f'Find item \033[32m{self.warehouse_list[el][0]}\033[0m,'
                          f' model \033[32m{self.warehouse_list[el][1]}\033[0m:'
                          f' {self.warehouse_list[el]}')
                    find_item = 1
            if find_item == 0:
                print(f'Item name: {name_office_equipment}, model {number_model} NOT found.')
        except:
            print('Error find_in_warehouse() class "WarehouseOfficeEquipment"')

    # подсчет суммы объектов на складе
    def sum_items_warehouse(self, name_office_equipment):
        try:
            self.sum_items = 0
            for el in range(len(self.warehouse_list)):
                if self.warehouse_list[el][0] == name_office_equipment:
                    self.sum_items += 1
            print(f'We have at Warehouse: {name_office_equipment}: {self.sum_items}')
        except:
            print('Error sum_items_warehouse() class "WarehouseOfficeEquipment"')

    # save to file warehouse
    def save_to_file(self, name_file_write):
        try:
            total = 0
            total_printers = 0
            total_scanners = 0
            total_copiers = 0
            with open(name_file_write, 'w', encoding='utf-8') as f_obj:
                for key, value in enumerate(range(len(self.warehouse_list)), 1):
                    f_obj.write(f'{key}. {self.warehouse_list[value]}\n')
                    if self.warehouse_list[value][0] == 'printer':
                        total_printers += 1
                    if self.warehouse_list[value][0] == 'scanner':
                        total_scanners += 1
                    if self.warehouse_list[value][0] == 'copier':
                        total_copiers += 1
                total = key
                print(
                    f'Total: {total},\tprinters: {total_printers},\tscanners: {total_scanners},\tcopiers: {total_copiers}',
                    file=f_obj)
                print(f'Writing to file: {name_file_write} ok')
        except IOError:
            print('Error save_to_file() class "WarehouseOfficeEquipment"a')
        except:
            print('Error save_to_file() class "WarehouseOfficeEquipment"')

    # удаление файла с данными склада
    def delete_file(self, name_file_write):
        try:
            os.remove(name_file_write)
        except FileNotFoundError:
            print('Error delete_file() class "WarehouseOfficeEquipment". File not found')
        except:
            print('Error delete_file() class "WarehouseOfficeEquipment"')

    def look_all_warehouse(self):
        try:
            print(f'Warehouse: {self.warehouse_list}')
        except:
            print('Error look_warehouse() class "WarehouseOfficeEquipment"')

    # резервное копирование файла наличия оргтехники на складе
    def backup_data(self, name_file_read, name_file_write_backup):
        try:
            with open(name_file_read, 'r', encoding='utf-8') as f_obj_1:
                with open(name_file_write_backup, 'w', encoding='utf-8') as f_obj_2:
                    shutil.copyfile(name_file_read, name_file_write_backup)
        except FileNotFoundError:
            print('Error backup_data() class "WarehouseOfficeEquipment". File not found')
        except:
            print('Error backup_data() class "WarehouseOfficeEquipment"')

    # --------------------------------------------------------------------

    # приводим к шаблону Surname N. P.
    @property
    def warehouse_manager(self):
        try:
            return self.__warehouse_manager
        except:
            print('Error! warehouse_manager() class "WarehouseOfficeEquipment"')

    @warehouse_manager.setter
    def warehouse_manager(self, warehouse_manager):
        try:
            sep = ' '  # separator
            surname, name, patronymic = warehouse_manager.split()

            # с помощью конкатенации строк приводим к шаблону Surname N. P.
            self.__warehouse_manager = surname.title() + sep + surname[:1].title() + \
                                       '.' + sep + patronymic[:1].title() + '.'
        except ValueError:
            print('Error ValueError! warehouse_manager.setter class "WarehouseOfficeEquipment"')
        except:
            print('Error! warehouse_manager.setter class "WarehouseOfficeEquipment"')

    # приветствие менджера
    def check_warehouse_manager(self):
        try:
            print(f'\n\t\t\t\t\t\t\t\t\t\tGood day, warehouse_manager: \033[33m\033[3m{self.warehouse_manager}\033[0m'
                  f'\n\t\t\t\t\t\t\t\t\t\t\033[33mThe sun\033[30m is still high, isn\'t it)')
        except:
            print('Error! check_warehouse_manager class "WarehouseOfficeEquipment"')

    @staticmethod
    def check_pwd(file_pwd, input_pwd):
        try:
            with open(file_pwd, encoding='utf-8') as f_obj_1:
                password_in_file = f_obj_1.read()
                password_user, salt_user = password_in_file.split(':')
            return password_user == hashlib.sha256(salt_user.encode() + input_pwd.encode()).hexdigest()
        except FileNotFoundError:
            print('Error check_pwd() class "WarehouseOfficeEquipment". File not found')
        except:
            print('Error! check_pwd() class "WarehouseOfficeEquipment"')

    # рачет хэша
    @staticmethod
    def hash_password(password):
        # uuid используется для генерации случайного числа
        salt = uuid.uuid4().hex
        print(hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt)
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    # меню программы
    @staticmethod
    def menu_input():
        try:
            menu_input = input('\n1.Add item\n2.Find item\n3.Sum item\n4.Show all items\n5.Delete item\n6.Save to file\n'
                               '7.Delete file\n8.Backup data\n9.Technical info\nExit press "q"\n\nEnter menu: ')
            return menu_input
        except:
            print('Error! menu_input() class "WarehouseOfficeEquipment"')


class OfficeEquipment:
    def __init__(self, name_office_equipment):
        self.name_office_equipment = name_office_equipment


class Printer(OfficeEquipment):
    def __init__(self, name_office_equipment, number_model, serial_number):
        super().__init__(name_office_equipment)
        self.data_printer = [name_office_equipment, number_model, serial_number]

    # формируем данные о принтере для отправки на склад
    def add_printer(self):
        return self.data_printer


print('\n\t\t\t\t\t\t\t\t\t\tProgram \033[33m"Warehouse Office Equipment"\033[30m')
menu_input = 'q'
login_attempts = 3
# модуль проверки пароля
while login_attempts != 0:
    responsible_warehouse_manager = str(
        input('\nEnter responsible warehouse manager separated by space bar(Surname Name Patronic): '))
    pwd_warehouse_manager = input('\nEnter administrator warehouse manager special key (pass: 1): ')
    if not WarehouseOfficeEquipment.check_pwd('pwd.txt', pwd_warehouse_manager):
        print(f'\n\033[31mAccess denied.\033[30mLogin attemps: {login_attempts - 1}')
        login_attempts -= 1
        sleep(1)
    else:
        print('\n\033[32mAccess granted\033[30m')
        order_1 = WarehouseOfficeEquipment(responsible_warehouse_manager)
        # fill some data for example
        print('\nFill some data for example:')
        printer_1 = Printer('printer', 'laserJet1', '1112')
        order_1.take_to_warehouse(printer_1.add_printer())
        printer_1 = Printer('scanner', 'Scan2', '1113')
        order_1.take_to_warehouse(printer_1.add_printer())
        printer_1 = Printer('printer', 'laserJet2', '1114')
        order_1.take_to_warehouse(printer_1.add_printer())
        # приветствие менджера
        order_1.check_warehouse_manager()
        menu_input = WarehouseOfficeEquipment.menu_input()
        break

while menu_input != 'q':
    if menu_input == '1':
        try:
            manual_automatic_mode = input('Fill manual mode, press - m or automatic mode, press - a : ')
            if manual_automatic_mode == 'm':
                print('\nAdd office equipment')
                name_office_equipment = input('Please, enter name_office_equipment(printer, scanner, copier): ')
                number_model = input('Please, enter number of model printer: ')
                serial_number = input('Please, serial number: ')
                printer_1 = Printer(name_office_equipment, number_model, serial_number)
                order_1.take_to_warehouse(printer_1.add_printer())
                menu_input = WarehouseOfficeEquipment.menu_input()
            elif manual_automatic_mode == 'a':
                print('\nAdd office equipment')
                name_office_equipment = 'printer'
                number_model = input('Please, enter number of model printer: ')
                serial_number = input('Please, serial number: ')
                printer_1 = Printer(name_office_equipment, number_model, serial_number)
                order_1.take_to_warehouse(printer_1.add_printer())
                menu_input = WarehouseOfficeEquipment.menu_input()
            else:
                print('Wrong letter!')
                menu_input = WarehouseOfficeEquipment.menu_input()
        except:
            print('error main() menu: add item')
    if menu_input == '2':
        try:
            print('\nFind office equipment:')
            name_office_equipment = input('Please, enter name office equipment: ')
            number_model = input('Please, number_model: ')
            order_1.find_in_warehouse(name_office_equipment, number_model)
            menu_input = WarehouseOfficeEquipment.menu_input()
        except:
            print('error main() menu: find item')
    if menu_input == '3':
        try:
            sum_what_item = input('Please, enter name office equipment: ')
            order_1.sum_items_warehouse(sum_what_item)
            menu_input = WarehouseOfficeEquipment.menu_input()
        except:
            print('error main() menu: sum item')
    if menu_input == '4':
        try:
            order_1.look_all_warehouse()
            menu_input = WarehouseOfficeEquipment.menu_input()
        except:
            print('error main() menu: Show all items')
    if menu_input == '5':
        try:
            name_model_to_delete = input('Please, enter model of the item office equipment to delete: ')
            are_you_sure = input('Are you sure DELETE office equipments? y - confirm ')
            if are_you_sure == 'y':
                order_1.delete_from_warehouse(name_model_to_delete)
                menu_input = WarehouseOfficeEquipment.menu_input()
            else:
                menu_input = WarehouseOfficeEquipment.menu_input()
                continue
        except:
            print('error main() menu: delete item')
    if menu_input == '6':
        try:
            name_file_to_save = input('Please, enter name of the file to save office equipments: ')
            order_1.save_to_file(name_file_to_save + '.txt')
            menu_input = WarehouseOfficeEquipment.menu_input()
        except:
            print('error main() menu: save to file')
    if menu_input == '7':
        try:
            name_file_to_delete = input('Please, enter name of the file to DELETE office equipments: ')
            are_you_sure = input('Are you sure DELETE office equipments? y - confirm ')
            if are_you_sure == 'y':
                order_1.delete_file(name_file_to_delete + '.txt')
                menu_input = WarehouseOfficeEquipment.menu_input()
            else:
                menu_input = WarehouseOfficeEquipment.menu_input()
                continue
        except:
            print('error main() menu: delete item')
    if menu_input == '8':
        try:
            name_file_source_backup = input('Please, enter name of source of the file to backup office equipments: ')
            name_file_destination_backup = input('Please, enter name of the destanation file to'
                                                 ' backup office equipments: ')
            order_1.backup_data(name_file_source_backup, name_file_destination_backup)
        except:
            print('error main() menu: backup file')
    if menu_input == '9':
        try:
        # о программе
            print('\nTechnical info')
            print(f'Interpretator python here: {sys.executable}')
            print(f'System: {sys.platform}')
            print('(C)2020 Author: Evgeny Rodkin\nhash:\n'
                  '840eeec32b3ba1870241ec4218925c44a077c066875cea44520d53bb82058a5b:289d5780734540ddbdba4b0ba59ae4f3')
            author_check = input('Please enter author of program you see:')
            if WarehouseOfficeEquipment.check_pwd('author.txt', author_check):
                print(f'author {author_check} is creator')
            else:
                print(f'author {author_check} is NOT creator')
            menu_input = WarehouseOfficeEquipment.menu_input()
        except:
            print('error main() menu: Technical info')

print('End the program.')
