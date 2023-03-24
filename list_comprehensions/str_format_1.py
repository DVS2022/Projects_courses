def name_and_number():
    """ Requests the name and number of the table and
    displays the appropriate message."""
    name = str(input('Введите имя: '))
    number = str(input('Введите номер столика: '))
    string = 'Добрый день, {0}! Ваш столик № {1}'.format(
        name,
        number
    )
    print(string)


name_and_number()
