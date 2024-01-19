def even_indices():
    """ Функция выводит элементы из списка только с четными индексами """
    list_1 = ['Вадим', 'Сергей', 'Александр', 'Максим', 'Евгения', 'Анастасия', 'Наталия', 'Ольга']
    list_even = []
    for i in range(len(list_1)):
        if (i-1) % 2:
            list_even.append(list_1[i])
    print('Турнирная сетка:', list_even)


even_indices()
