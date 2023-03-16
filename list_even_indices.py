def even_indices():
    """ Функция выводит элементы из списка только с четными индексами """
    list_1 = ['Вадим', 'Сергей', 'Александр', 'Максим', 'Евгения', 'Наталия', 'Анастасия', 'Ольга']
    list_even = []
    for i in range(len(list_1)):
        if i % 2:
            list_even.append(list_1[i])
    print('Турнирная сетка:', list_even)


even_indices()
