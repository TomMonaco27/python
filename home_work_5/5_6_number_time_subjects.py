"""
Lesson 5 Task 6.
Program "Count hours of subjects"
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def number_of_lectures_in_subject(name_file_read, mode_read, encoding_file):
    try:
        sum_time_subject = 0
        with open(name_file_read, mode_read, encoding=encoding_file) as f_obj:
            print(f'1. Opening and calculating sum in file: {name_file_read}..')
            read_string_list = f_obj.readlines()
            for object in read_string_list:
                words = object.split()  # разделяем строку на списко с элементами, пример Информатика: 100(л) 50(пр) 20(лаб)
                len_words = len(words)  # считаем сколько элементов в строке
                for i in range(1, len_words):  # берем каждый элемент, т.е. 100(л)
                    time_subjects = words[i].split("(")   # отделяем по скобке элементы времени лекций, т.е. 100(л), 50(пр), 20(лаб) # получаем sum = ['100', 'л)']
                    if time_subjects[0] != chr(45):           # отсекаем пустые элементы времени лекций
                        sum_time_subject += int(time_subjects[0])
                dict_subjects[words[0]] = sum_time_subject
                sum_time_subject = 0
            print(f'\nDictionary is {dict_subjects}')
    except IOError:
        print(f'Error number_of_lectures_in_subject(). Input-output error! Please, check check file existence {name_file_read}')
    except:
        print('Error number_of_lectures_in_subject()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')


def main():
    global separator, name_file_read, mode_read, encoding_file, dict_subjects, list_subjects
    dict_subjects = {}
    list_subjects = []
    name_file_read = 'lesson_5_task_6.txt'
    mode_read = 'r'
    encoding_file = "UTF-8"
    try:
        print('Program "Count hours of subjects"')
        number_of_lectures_in_subject(name_file_read, mode_read, encoding_file)
    except:
        print(
            'Error main()! Something wrong, but don\'t worry, be happy.'
            ' Maybe next time, buy yourself a ice cream :)')
    finally:
            print('End the program.')


if __name__ == '__main__':
    main()