import random


def sums_values():
    """ Makes two random lists and makes the third one through
    the list comprehensions.
    """
    lst_1 = [random.randint(100, 200) for _ in range(10)]
    lst_2 = [random.randint(100, 200) for _ in range(10)]
    lst_3 = [('Не повезло' if lst_1[i] + lst_2[i] > 300
              else 'Повезло!') for i in range(10)]
    print('Первый рандомный список:', lst_1)
    print('Второй рандомный список:', lst_2)
    print('Третий итоговый список:', lst_3)


sums_values()
