def add_and_remove():
    """ Функция добавляет или удаляет необходимые элементы из списка исходя из
    потребностей пользователя. """
    lst = ['Первый', 'Второй', 'Третий', 'Четвертый', 'Пятый']
    answer = ''
    while answer != 'Домой':
        count = len(lst)
        print(f'Всего за столом {count} человек: {lst}')
        answer = str(input('Гость пришел или ушел?: '))
        if answer == 'пришел':
            guest = str(input('Напишите имя гостя: '))
            if count >= 5:
                print(f'За столом нет мест! Сорян, {guest}')
            else:
                print(f'Проходите за стол, {guest}!')
                lst.append(guest)
        elif answer == 'ушел':
            guest = str(input('Напишите имя гостя: '))
            if guest in lst:
                lst.remove(guest)
                print(f'Ушел из-за стола, {guest}.')
            else:
                print(f'Нет! {guest} не за столом!')
        elif answer == 'Домой':
            print('Вот и всё!')
            break
        else:
            print('Неизвестная команда!')
    print('Игра закончена')


add_and_remove()
