def update_and_get():
    """ Concatenates two dictionaries and returns data on request. """
    dict_1 = {'Первое': 1000, 'Второе': 2000, 'Третье': 3000}
    dict_2 = {'Четвертое': 4000, 'Пятое': 5000, 'Шестое': 6000}
    dict_2.update(dict_1)
    item = input('Введите запрос: ')
    if dict_2.get(item) is None:
        print('Ошибка! Наименование отсутствует!')
    else:
        print(f'Количество запрашиваемого продукта:', dict_2.get(item))


update_and_get()

