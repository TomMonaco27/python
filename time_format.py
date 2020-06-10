# Lesson 1 Task 2
# Программа "Time format"
# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

print('Программа "Time Format"')
input_seconds = int(input('Введите время в секундах: '))
hours = int(input_seconds / 3600)
minutes = int((input_seconds - hours * 3600) / 60)
seconds = int(input_seconds - hours * 3600 - minutes * 60)
print(f'Время в формате чч:мм:cc : {hours:02}:{minutes:02}:{seconds:02}')
