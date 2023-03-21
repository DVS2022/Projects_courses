def counting_rhyme():
    """ Функция создает список из N человек, запрашивает число К -
    счет через который будут выбывать игроки. Выводит последнего игрока. """
    amount = int(input('Введите количество человек: '))
    lst = list(range(1, amount+1))
    number = int(input('Введите номер счета: '))
    print(f'Выбывает каждый {number} человек')
    i = 0
    while len(lst) > 1:
        print('Текущий список участников:', lst)
        print(f'Начало отсчета с номера: {lst[i]}')
        i = (i + number - 1) % len(lst)
        print('Счет остановился на игроке №', lst[i], '\n')
        lst.pop(i)
        i = i % len(lst)
    print('Последний участник:', lst)


counting_rhyme()
