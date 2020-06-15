# Lesson 2 Task 6.
# Программа "Goods analytics"
# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (
# характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя. Пример готовой структуры: [
#
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#
# ] Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров. Пример: {

# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]

# }

dict_goods_in = {}  # словарь товаров, введенный пользователем
tuple_goods_in = ()
list_goods_in = []
list_name_goods = []
list_price_goods = []
list_amount_goods = []
list_units_goods = []
analytics_dict = {}
num_order_in = 1  # порядковый номер при заполнении структуры кортеж-словарь (ввод пользователем)
num_order_out = 1 # порядковый номер для правильного заполнения списков значений-характеристик
stop_input = 'y'

print('Программа "Goods analytics"')
while True:  # заполнение структуры данных "Товары"
    name_goods = input('Введите название товара: ')
    price_goods = input('Введите цену товара: ')
    amount_goods = input('Введите количество товара: ')
    units_goods = input('Введите единицы товара, например шт., уп.: ')

    dict_goods_in['название'] = name_goods
    dict_goods_in['цена'] = price_goods
    dict_goods_in['количество'] = amount_goods
    dict_goods_in['единицы'] = units_goods

    tuple_goods_in = list(tuple_goods_in)  # для удобства работы преобразование в список

    tuple_goods_in.append(num_order_in)  # добавление номера по порядку "n" в связку кортеж-словарь (n, {key:value})
    tuple_goods_in.append(dict_goods_in)  # добавление словаря в связку кортеж-словарь (n, {key:value})

    tuple_goods_in = tuple(tuple_goods_in)  # возвращаем в кортеж, т.к. по условию задачи
    list_goods_in.append(tuple_goods_in)  # заполняем список собранным кортежом (n, {key:value})

    dict_goods_in = {}  # очистка словаря для следующей итерации ввода данных пользователем
    tuple_goods_in = ()  # очистка кортежа для следующей итерации ввода данных пользователем

    stop_input = input('Для завершения ввода введите "y": ')
    if stop_input == 'y':  # выход из ввода
        break

    num_order_in += 1

print('\nВведенный список:')
for el_list_in in list_goods_in:
    print(f'{el_list_in}')
# реализуем аналитику о товарах, заполняем словарь
for el_list_out in list_goods_in:  # открыли list
    num_order_out = 1
    tuple_goods_out = list(el_list_out)  # преобразовали кортеж в список для удобства работы
    for key_tuple_out in tuple_goods_out[1]:
        if num_order_out == 1:
            list_name_goods.append(tuple_goods_out[1].get(key_tuple_out))
        if num_order_out == 2:
            list_price_goods.append(tuple_goods_out[1].get(key_tuple_out))
        if num_order_out == 3:
            list_amount_goods.append(tuple_goods_out[1].get(key_tuple_out))
        if num_order_out == 4:
            list_units_goods.append(tuple_goods_out[1].get(key_tuple_out))
        num_order_out += 1

# заполняем итоговый аналитический словарь "analytics_dict" c помощью заранее собранных списков
analytics_dict['название'] = list_name_goods
analytics_dict['цена'] = list_price_goods
analytics_dict['количество'] = list_amount_goods
list_units_goods = list(set(list_units_goods))  # избавляемся от дублирующих элементов, путем преобразованием во множество
analytics_dict['ед'] = list_units_goods

# выводим итоговый аналитический словарь "analytics_dict"
print('\nИтоговый аналитический словарь "Analytics dict": ')
for key_analitic_dict, val_analitic_dict in analytics_dict.items():
    print(f'{key_analitic_dict} : {val_analitic_dict}')
