def min_and_pop():
    """ Finds the smallest value in the dictionary and removes
    that element.
    """
    dict_1 = {'Первое': 1000, 'Второе': 10, 'Третье': 3000,
              'Четвертое': 40.4, 'Пятое': 5000, 'Компот': 6000}

    value = sum(dict_1.values())
    min_value_name = min(dict_1, key=dict_1.get)
    min_value = dict_1[min_value_name]
    dict_1.pop(min_value_name)
    print('Итого сумма:', value)
    print(min_value_name, '- самое дешевое, его стоимость:', min_value)
    print('Словарь без самого дешевого продукта:', dict_1)


min_and_pop()
