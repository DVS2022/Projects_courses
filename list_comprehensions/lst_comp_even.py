def even_numb():
    """ Creates a list of even numbers in a specific range. """
    start = int(input('Введите начало списка: '))
    stop = int(input('Введите конец списка: '))
    lst = [x for x in range(start, stop+1) if x % 2 == 0]
    print(lst)


even_numb()
