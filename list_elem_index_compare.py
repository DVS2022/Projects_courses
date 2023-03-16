def compare_value_index():
    """ Функция принимает количество клеток и """
    amount = int(input('Введите количество клеток: '))
    list_1 = [5, 3, 1, 7, 4, 2, 15, 5, 7, 54]
    improper_list = []
    improper_index = []
    for i in range(amount):
        print(f'Эффективность {i + 1} клетки {list_1[i]}')
        if (i + 1) > list_1[i]:
            improper_list.append(list_1[i])
            improper_index.append(i+1)
    print('Неподходящие значения:\t\t\t', improper_list)
    print('Неподходящие индексы значений:\t', improper_index)


compare_value_index()
