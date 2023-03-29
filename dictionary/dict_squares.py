def squares():
    """ The user enters a number and gets a dictionary with squares
    up to that number.
    """
    number = int(input('Введите число: '))
    dict_of_squares = dict()
    for i in range(1, number+1):
        dict_of_squares[i] = i**2
    print(dict_of_squares)


squares()
