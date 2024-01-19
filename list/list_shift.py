def shift_foo():
    """ Функция сдвигает список на N элементов вправо """
    shift = int(input('Введите значение сдвига: '))
    lst = [-10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    shift_lst = []
    for i in range(len(lst)):
        j = i - shift
        if j >= len(lst):
            j = j - len(lst)
            shift_lst.append(lst[j])
        else:
            shift_lst.append(lst[j])
    print('Изначальный список:', lst)
    print('Список после сдвига:', shift_lst)


shift_foo()
