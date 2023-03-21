def inflation_calculation():
    """ Takes the quantity of goods and their prices, calculates
    the sum of the prices of these goods and inflation for 2 years
    in advance
    """
    amount = int(input('Введите количество товаров: '))
    lst = [int(input('Стоимость товара: ')) for _ in range(amount)]
    print(lst)
    increase_1 = float(input('Введите процент повышения в этом году: '))
    increase_2 = float(input('Введите процент повышения в следующем году: '))
    result_1 = [percent_calc(increase_1, i_price) for i_price in lst]
    result_2 = [percent_calc(increase_2, i_price) for i_price in result_1]
    print(f'Результаты инфляции:\nИзначальная сумма товаров: {round(sum(lst), 2)}'
          f'\nПервый год после повышения: {round(sum(result_1), 2)} '
          f'\nВторой год после повышения: {round(sum(result_2), 2)}')


def percent_calc(percent, price):
    """ Returns the price with inflation added """
    return round(price * (1 + percent / 100), 2)


inflation_calculation()
