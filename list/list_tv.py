def favorites():
    """ Функция из определенного списка ТВ каналов добавляет определенные каналы
    в избранное, также ставит их на выбранные места и удаляет при необходимости. """
    channels = ['Первый', 'Второй', 'Третий', 'Четвертый', 'Пятый']
    favor_list = []
    while True:
        print('Список ТВ:', channels)
        print('Избранное:', favor_list, '\n')
        tv_ch = str(input('Введите название канала из списка: '))
        if tv_ch in channels:
            command = str(input('Введите команду: "Добавить", "Вставить", "Удалить", "Выйти": '))
            if command == 'Добавить':
                if tv_ch in favor_list:
                    print('Такой канал уже есть в списке!\n')
                    continue
                else:
                    favor_list.append(tv_ch)
            elif command == 'Вставить':
                if tv_ch in favor_list:
                    print('Такой канал уже есть в списке!\n')
                    continue
                else:
                    ind_tv = int(input('Введите номер места: '))
                    favor_list.insert(ind_tv-1, tv_ch)
            elif command == 'Удалить':
                if tv_ch in favor_list:
                    favor_list.remove(tv_ch)
                else:
                    print('Такой канал отсутствует в списке\n!')
            elif command == 'Выйти':
                break
        else:
            print('Такого канала в списке нет!')


favorites()
