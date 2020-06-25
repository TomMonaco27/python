"""
Lesson - 5 Task - 4.
Program "File translation"
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


from googletrans import Translator


def file_translate():
    try:
        cr = '\n'
        sb = ' '
        with open('lesson_5_task_4.txt', 'r', encoding="UTF-8") as f_obj:
            print('1. Opening file: lesson_5_task_4.txt..')
            read_string_list = f_obj.readlines()
            translator = Translator()  #  initialization the Translator object
        with open('lesson_5_task_4_1.txt', 'w', encoding="UTF-8") as f_obj_2:
            print('2. Opening file: lesson_5_task_4_1.txt..')
            for string in read_string_list:
                words_string = string.split()
                trans_to_rus = translator.translate(words_string[0], dest='ru')
                print('Translating file: lesson_5_task_4.txt..')
                write_string_list = trans_to_rus.text, sb, words_string[1], sb, words_string[2], cr
                f_obj_2.writelines(write_string_list)
            print('4. Writing to file: lesson_5_task_4_1.txt..')
    except IOError:
        print('Input-output error! Please, check check file existence "lesson_5_task_3.txt"')
    except:
        print('Error! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')


def main():
    try:
        print('Program "File translation"')
        print('Need internet for work of the program ""')
        file_translate()
    except:
        print('Error main()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')
    finally:
        print('End the program.')


if __name__ == '__main__':
    main()



