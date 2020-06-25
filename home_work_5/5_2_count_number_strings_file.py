"""
Lesson 5 Task 2.
Program "count number of strings in a file"
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


def count_strings_file():
    try:
        with open('lesson_5_task_2.txt', 'r', encoding="UTF-8") as f_obj:
            print('1. Opening file: lesson_5_task_2.txt..ok')
            read_string_list = f_obj.readlines()
            print(f'Total lines in file: {len(read_string_list)}')
            for num, el in enumerate(read_string_list):
                words_in_string = len(el.split())
                print(f'Words in string {num} is {words_in_string}')
    except IOError:
        print('Error count_strings_file(). Input-output error!')
    except:
        print('Error count_strings_file()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')


def main():
    try:
        print('Program "count number of strings in the file"')
        count_strings_file()
    except:
        print('Error main()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')
    finally:
        print('End the program.')


if __name__ == '__main__':
    main()

