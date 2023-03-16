def degree_table():
    """ Функция добавляет в список числа и возводит их во 2ю, 4ю, 6ю степени. """
    list_numbers = [2, 5, 9, 12]
    while True:
        number = int(input('Введите число: '))
        list_numbers.append(number)
        print('Текущий список:', list_numbers)
        for i in list_numbers:
            print(i ** 2, i ** 4, i ** 6)
        print()


degree_table()
