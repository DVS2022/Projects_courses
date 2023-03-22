import random


def del_interval():
    """ Removes part of the list at the given interval. """
    lst_1 = [random.randint(0, 100) for _ in range(10)]
    print(lst_1)
    start = int(input('Введите начало интервала для удаления элементов: '))
    stop = int(input('Введите конец интервала для удаления элементов '
                     '(включительно): '))
    print([lst_1[i] for i in range(len(lst_1)) if
           i not in range(start-1, stop)])


del_interval()
