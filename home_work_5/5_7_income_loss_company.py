"""
lesson 5 Task 7.
Program "is income or loss company"
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""


import json


def is_income_or_loss(name_file_read, mode_read, encoding_file):
    average_profit_value = 0
    count_positive_profit = 0
    try:
        with open(name_file_read, mode_read, encoding=encoding_file) as f_obj:
            print(f'1. Opening file: {name_file_read}:')
            read_string_list = f_obj.readlines()
            print(f'list in file: {read_string_list}')
            for el in read_string_list:
                read_words_list = el.split()
                balance_firm = float(read_words_list[2]) - float(read_words_list[3])
                if balance_firm > 0:
                    count_positive_profit += 1
                    average_profit_value += balance_firm
                for i in range(1, len(read_words_list)):
                    dict_firms[read_words_list[0]] = balance_firm
            average_profit_value = round((average_profit_value / count_positive_profit), 4)
            average_profit_dict['average_profit'] = average_profit_value
            json_list.append(dict_firms)
            json_list.append(average_profit_dict)
            print(f'Final json_list is : {json_list}')
    except IOError:
        print(f'Error is_income_or_loss().'
              f'Input-output error! Please, check check file existence {name_file_read}')
    except:
        print('Error is_income_or_loss! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')


def write_json(name_json_write, mode_write, encoding_file, json_list):
    try:
        with open(name_json_write, mode_write, encoding=encoding_file) as write_json:
            json.dump(json_list, write_json, indent=1)
            print(f'2. Writing to {name_json_write}:')
            return print('OK')
    except IOError:
        print(f'Error write_json(). Input-output error! '
              f'Please, check check file existence {name_json_write}')
    except:
        print('Error write_json()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')


def main():
    global name_file_read, mode_read, encoding_file, dict_firms, average_profit_dict, json_list
    json_list = []
    average_profit_dict = {}
    dict_firms = {}
    name_file_read = 'lesson_5_task_7.txt'
    name_json_write = 'lesson_5_task_7.json'
    mode_read = 'r'
    mode_write = 'w'
    encoding_file = "UTF-8"
    try:
        print('Program "is income or loss company"')
        is_income_or_loss(name_file_read, mode_read, encoding_file)
        write_json(name_json_write, mode_write, encoding_file, json_list)
    except:
        print(
            'Error main()! Something wrong, but don\'t worry, be happy.'
            ' Maybe next time, buy yourself a ice cream :)')
    finally:
        print('End the program.')


if __name__ == '__main__':
    main()
