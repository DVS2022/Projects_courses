def prices_sum():
    """ From a given list of dishes, the user selects the desired
    ones and the function calculates their total cost.
    """
    dict_all = {'Первое': 10.5, 'Второе': 22.5, 'Третье': 25.5,
                'Четвертое': 27.5, 'Пятое': 29.5, 'Шестое': 32.5,
                'Седьмое': 35.5, 'Восьмое': 37.5, 'Девятое': 39.5
                }
    dict_user = dict()
    amount = int(input('Введите количество блюд: '))
    for i in range(amount):
        dish = input('Введите название блюда: ')
        if dish in dict_all:
            price = dict_all[dish]
            dict_user[dish] = price
        else:
            print('Нет такого блюда!')
    total_price = sum(dict_user.values())
    print('Список блюд:', dict_user)
    print('Общая стоимость:', total_price)


prices_sum()
