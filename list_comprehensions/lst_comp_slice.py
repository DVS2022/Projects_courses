import random


def slice_the_list():
    """ Demonstrates various ways to use list slicing. """
    lst_1 = [random.randint(-100, 100) for _ in range(10)]
    print('Основной список:\t\t\t\t\t\t', lst_1)
    print('Первые пять элементов списка:\t\t\t', lst_1[:5])
    print('Все элементы кроме последних трех:\t\t', lst_1[:-3])
    print('Элементы списка с четными индексами:\t', lst_1[::2])
    print('Элементы списка с нечетными индексами:\t', lst_1[1::2])
    print('Список в обратном порядке:\t\t\t\t', lst_1[::-1])
    print('Список в обратном порядке через 1:\t\t', lst_1[::-2])


slice_the_list()
