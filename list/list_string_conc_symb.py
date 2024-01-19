def concatenation():
    """ Функция объединяет введенные строки по принципу - где больше
    '!' и '?' знаков, та строка и ставиться на первое место. """
    first_massage = str(input('Введите первое сообщение: '))
    second_massage = str(input('Введите второе сообщение: '))
    first_mas_lst = list(first_massage)
    second_mas_lst = list(second_massage)
    count_1 = 0
    count_2 = 0
    for i in range(len(first_mas_lst)):
        if first_mas_lst[i] == '!' or first_mas_lst[i] == '?':
            count_1 += 1
    for i in range(len(second_mas_lst)):
        if second_mas_lst[i] == '!' or second_mas_lst[i] == '?':
            count_2 += 1
    if count_1 > count_2:
        print('Вывод (знаков больше в 1й строке):', first_massage + second_massage)
    elif count_1 < count_2:
        print('Вывод (знаков больше во 2й строке):', second_massage + first_massage)
    else:
        print('Количество знаков совпадает!')


concatenation()
