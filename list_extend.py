def merge():
    """ Функция объединяет 4 списка битов и подсчитывает количество нулей """
    lst = []
    first_list = [0, 1, 1, 0, 1, 1, 1, 1]
    second_list = [0, 1, 0, 1, 1, 0, 1]
    third_list = [0, 1, 1, 1, 0, 0, 0, 1]
    fourth_list = [1, 1, 0, 1, 1, 1, 0, 1]
    print(first_list)
    print(second_list)
    print(third_list)
    print(fourth_list)
    lst.extend(first_list)
    lst.extend(second_list)
    lst.extend(third_list)
    lst.extend(fourth_list)
    print('Объединенный список:', lst)
    print('Количество нулей: ', lst.count(0))


merge()
