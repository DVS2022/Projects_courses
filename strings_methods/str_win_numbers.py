def win_numbers():
    """ Requests the template of congratulations on winning the lottery.
    The user enters the names and numbers of the winners. Displays
    congratulations and a list of winners.
    """
    greeting = input('Введите шаблон поздравления ({name}, {number}): ')
    names = input('Введите имена через запятую: ').split(', ')
    numbers = input('Введите выигрышные номера через запятую: ').split(', ')
    all_lst = ''
    for i in range(len(names)):
        print(greeting.format(
            name=names[i],
            number=numbers[i]
        ))
        all_lst = [' '.join([names[i], numbers[i]]) for
                   i in range(len(names))]

    all_str = ', '.join(all_lst)
    print(all_str)


win_numbers()
