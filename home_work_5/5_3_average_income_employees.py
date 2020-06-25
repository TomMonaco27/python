"""
Lesson 5 Task 3.
Program "average income of employees"
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


def average_employee_income():
    try:
        amount_of_income = 0
        with open('lesson_5_task_3.txt', 'r', encoding="UTF-8") as f_obj:
            print('1. Opening file: lesson_5_task_3.txt..ok')
            read_string_list = f_obj.readlines()
            number_of_employee = len(read_string_list)
            print(f'The company has {number_of_employee} employees')
            for el in read_string_list:
                data_in_string = el.split()
                if float(data_in_string[1]) < 20000:
                    print(f'Employee {data_in_string[0]} has a salary of less than 20.000')
                amount_of_income += float(data_in_string[1])
            print(f'Average employee income is {(amount_of_income / number_of_employee):.4f}')
    except IOError:
        print('Input-output error! Please, check check file existence "lesson_5_task_3.txt"')
    except ZeroDivisionError:
        print('Error! Division by zero! Check number of employee. You work without workers? :)')
    except:
        print('Error! Something wrong, but don\'t worry, be happy. Maybe next time, buy yourself a ice cream :)')
    finally:
        print('End the program.')


def main():
    print('Program "average income of employees"')
    average_employee_income()


if __name__ == '__main__':
    main()
