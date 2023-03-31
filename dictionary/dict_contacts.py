def contacts():
    """ Creates a list of contacts. """
    name = ''
    cont_dict = dict()
    while name != 'выход':
        print('Текущие контакты:')
        for i in cont_dict:
            print(i, '-', cont_dict[i])
        name = input('Введите имя: ')
        number = int(input('Введите номер: '))
        if name in cont_dict:
            print('Ошибка! Имя существует!')
        else:
            cont_dict[name] = number


contacts()
