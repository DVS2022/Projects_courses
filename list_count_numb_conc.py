def count_and_conc():
    """ Функция объединяет списки, подсчитывает количество необходимых цифр и удаляет их. """
    lst_1 = [1, 1, 2, 2, 3, 3]
    lst_2 = [2, 2, 3, 3, 4, 4]
    lst_3 = [3, 4, 3, 4, 5, 5]
    lst_1.extend(lst_2)
    x = lst_1.count(3)
    print('Количество троек после объединения lst_1 и lst_2:', x)
    for i in range(x):
        lst_1.remove(3)
    lst_1.extend(lst_3)
    print('Количество пятерок после объединения lst_1 и lst_3:', lst_1.count(5))
    print(lst_1)


count_and_conc()
