def dish_orders():
    """ Dictionary containing the orders of each customer, where each
    key in the dictionary is a customer name, and the value is another
    dictionary with dishes ordered by that customer and their
    respective quantities.
    """
    amount_orders = int(input('Введите количество заказов: '))
    orders = dict()
    for i in range(amount_orders):
        customer, dish, quantity = input(f'{i+1} заказ: ').split()
        if customer not in orders:
            orders[customer] = {}
        if dish not in orders[customer]:
            orders[customer][dish] = 0
        orders[customer][dish] += int(quantity)
    print(orders)

    for customer in orders:
        print(customer, 'заказал:')
        for dish in orders[customer]:
            quantity = orders[customer][dish]
            print(f'{dish} - {quantity}', 'шт.')
        print()


dish_orders()
