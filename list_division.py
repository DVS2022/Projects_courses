def division():
    """ Функция запрашивает количество чисел и делит их на ячейки. (Список в списке) """
    amount_numbers = int(input('Введите количество чисел: '))
    cell = int(input('Введите количество чисел в ячейке: '))
    num_lst = []
    start = 1
    if amount_numbers % cell != 0:
        print(f'Количество номеров ({amount_numbers}) не делится на количество ячеек ({cell})!')
    else:
        for i in range(amount_numbers // cell):
            num_lst.append(list(range(start, start + cell)))
            start += cell
    print(num_lst)


division()
