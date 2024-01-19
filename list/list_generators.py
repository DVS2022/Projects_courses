def generate_and_sort():
    """ Функция генерирует списки, объединяет их и сортирует. """
    lst_1 = list(range(1, 102, 5))
    lst_2 = list(range(1, 107, 7))
    print('Список от 1 до 101 с шагом 5:', lst_1)
    print('Список от 1 до 106 с шагом 7:', lst_2)
    lst_1.extend(lst_2)
    print('Объединенный список:', lst_1)
    lst_1.sort()
    print('Отсортированный список:', lst_1)


generate_and_sort()
