def cubes_and_squares():
    """ Функция создает списки квадратов и кубов чисел в
    заданном диапазоне.
    """
    start = int(input('Введите начало списка: '))
    stop = int(input('Введите конец списка: '))
    print(f'Список квадратов чисел от {start} до {stop}',
          [x**3 for x in range(start, stop+1)])
    print(f'Список кубов чисел от {start} до {stop}',
          [x**2 for x in range(start, stop+1)])


cubes_and_squares()
