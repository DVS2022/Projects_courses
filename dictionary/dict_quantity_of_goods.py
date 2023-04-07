def quantity_of_goods():
    """ Iterates over each stock entry in the store dictionary,
    summing up the total quantity and cost. Finally, prints out
    the total quantity and cost for each item.
    """
    goods = {
        'Первое': '11111',
        'Второе': '22222',
        'Третье': '33333',
        'Четвертое': '44444',
        'Пятое': '55555',
    }

    store = {
        '11111': [
            {'quantity': 100, 'price': 1000},
        ],
        '22222': [
            {'quantity': 200, 'price': 2000},
            {'quantity': 300, 'price': 3000},
        ],
        '33333': [
            {'quantity': 400, 'price': 4000},
            {'quantity': 500, 'price': 5000},
        ],
        '44444': [
            {'quantity': 600, 'price': 6000},
            {'quantity': 700, 'price': 7000},
            {'quantity': 800, 'price': 8000},
        ],
        '55555': [
            {'quantity': 900, 'price': 9000},
            {'quantity': 1000, 'price': 10000},
            {'quantity': 1100, 'price': 11000},
        ],
    }

    for item, code in goods.items():
        total_quantity = 0
        total_cost = 0
        for i in store[code]:
            total_quantity += i['quantity']
            total_cost += i['quantity'] * i['price']
        print(f'{item} - {total_quantity} шт., общей стоимостью {total_cost}')


quantity_of_goods()
