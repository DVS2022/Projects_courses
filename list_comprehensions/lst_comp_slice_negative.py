import random


def slice_negative():
    """ Generates a random list of numbers discards negative values
    and calculates their sum.
    """
    lst_1 = [random.randint(-100, 100) for _ in range(10)]
    lst_copy = lst_1[:]
    lst_refactor = [(0 if x < 0 else x) for x in lst_copy]
    print(lst_copy)
    print(lst_refactor)
    print('Сумма отрицательных значений:', sum(lst_copy) - sum(lst_refactor))


slice_negative()
