def strange_list():
    """ Generates a list of a certain length, even places are symbols,
    and odd numbers are equal to the remainder of dividing their number by 7.
    """
    num = int(input('Введите длину списка: '))
    lst = ['Ч' if i % 2 == 0 else i % 7 for i in range(num)]
    print(lst)


strange_list()
