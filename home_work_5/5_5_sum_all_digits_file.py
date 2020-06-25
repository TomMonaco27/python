"""
Lesson 5 Task 5.
Program "Sum of all digits in the file"
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def fill_file(name_file_write, mode_add_write, encoding_file):
    try:
        len_digit = range(1, 100)
        with open(name_file_write, mode_add_write, encoding=encoding_file) as f_obj:
            print(f'1. Opening and filling file: {name_file_write}..')
            for i in len_digit:
                f_obj.write(str(i) + separator)
        return print('OK')
    except IOError:
        print(f'Error fill_file(). Input-output error!'
              f' Please, check check file existence {name_file_write}')
    except:
        print('Error fill_file()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')


def sum_in_file(name_file_read, mode_read, encoding_file):
    try:
        sum_digits_in_file = 0
        with open(name_file_read, mode_read, encoding=encoding_file) as f_obj:
            print(f'2. Opening and calculating sum in file: {name_file_read}..')
            read_string_list = (f_obj.read()).split()
            for num in read_string_list:
                sum_digits_in_file += float(num)
        return sum_digits_in_file
    except IOError:
        print(f'Error sum_in_file(). Input-output error!'
              f' Please, check check file existence {name_file_read}')
    except:
        print('Error sum_in_file()! Something wrong, but don\'t worry, be happy. '
              'Maybe next time, buy yourself a ice cream :)')


def main():
    global separator
    separator = ' '  # separator of digits in file
    name_file_read = 'lesson_5_task_5.txt'
    name_file_write = name_file_read
    mode_add_write = 'a'
    mode_read = 'r'
    encoding_file = "UTF-8"
    try:
        print('Program "Sum of all numbers in file"')
        fill_file(name_file_write, mode_add_write, encoding_file)
        print(f'Sum of all digits in file is {sum_in_file(name_file_read, mode_read, encoding_file)}')
    except:
        print('Error main()! Something wrong, but don\'t worry, be happy. Maybe next time, buy yourself a ice cream :)')
    finally:
        print('End the program.')


if __name__ == '__main__':
    main()