def debt():
    """ Функция выполняет расчет задолженностей между контрагентами. """
    amount_people = int(input('Введите количество контрагентов: '))
    amount_debt_notes = int(input('Введите количество расписок: '))
    lst_all = [[0] * 2 for i in range(amount_people)]
    for i in range(len(lst_all)):
        lst_all[i][0] = i+1
    print(lst_all)

    for i in range(amount_debt_notes):
        print('Расписка №', i+1)
        to_man = int(input('Кому должны?: '))
        from_man = int(input('Кто должен?: '))
        if to_man != from_man:
            summ = int(input('Сколько должен?: '))
            lst_all[to_man-1][1] += summ
            lst_all[from_man-1][1] -= summ
        else:
            print('Самому себе нельзя задолжать!')

    for i in range(len(lst_all)):
        print(f'Баланс контрагента № {i+1} = {lst_all[i][1]}')


debt()
