"""
Lesson 5 Task 1.
Program "write_input_in_file"
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def write_file():
    input_str = 0
    try:
        with open('lesson_5_task_1.txt', 'w', encoding="UTF-8") as f_obj:
            print('1. Creating new file: lesson_5_task_1.txt..ok')
            while input_str != '':
                input_str = input('Enter string to write in file: ')
                input_list.append(input_str)
            input_str_file = '\n'.join(input_list)
            f_obj.writelines(input_str_file)
            print('2. Writing to file...ok')
    except IOError:
        print('Input-output error!')
    except:
        print('Error write_file()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')


def main():
    global input_list
    input_list = []
    try:
        print('Program "write_input_in_file"')
        print('Stop input - clear string')
        write_file()
    except:
        print('Error main()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')
    finally:
        print('End the program.')


if __name__ == '__main__':
    main()


# --------------------------------------------------------2------------------------------------------------------------


def write_file():
    input_str = 0
    try:
        with open('lesson_5_task_1_1.txt', 'w', encoding="UTF-8") as f_obj:
            print('1. Creating new file: lesson_5_task_1_1.txt..ok')
            while input_str != '':
                input_str = input('Enter string to write in file: ')
                print(input_str, file = f_obj) # запись в файл с помощью print
            print('2. Writing to file...ok')
    except IOError:
        print('Input-output error!')
    except:
        print('Error write_file()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')


def main():
    try:
        print('Program "write_input_in_file"')
        print('Stop input - clear string')
        write_file()
    except:
        print('Error main()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')
    finally:
        print('End the program.')


if __name__ == '__main__':
    main()


# --------------------------------------------------------3------------------------------------------------------------


def write_file():
    global final_str
    input_str = 0
    try:
        f_obj = open('lesson_5_task_1_2.txt', 'w', encoding="UTF-8")
        print('1. Creating new file: lesson_5_task_1_2.txt..ok')
        while input_str != '':
            input_str = input('Enter string to write in file: ')
            final_str = final_str + input_str + '\n'
        f_obj.write(final_str) # запись в файл с помощью write
        print('2. Writing to file...ok')
    except IOError:
        print('Error write_file(). Input-output error!')
    except:
        print('Error write_file()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')
    finally:
        f_obj.close()


def main():
    global final_str
    final_str = ''
    try:
        print('Program "write_input_in_file"')
        print('Stop input - clear string')
        write_file()
    except:
        print('Error main()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')
    finally:
        print('End the program.')


if __name__ == '__main__':
    main()
