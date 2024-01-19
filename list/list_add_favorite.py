def add_to_favorite():
    """ Функция принимает несколько значений str, если они есть в заданном
    списке добавляет их в отдельный список """
    lst = ['Первый', 'Второй', 'Третий', 'Четвертый', 'Пятый']
    favorite_lst = []
    print('Список доступных каналов ТВ:', lst)
    amount_channels = int(input('Сколько каналов хотите добавить?: '))
    flag = False
    for _ in range(amount_channels):
        favorite = str(input('Введите канал ТВ для добавления в избранное: '))
        for i in range(len(lst)):
            if lst[i] == favorite:
                favorite_lst.append(favorite)
                print('Канал добавлен в избранное')
                flag = True
        if not flag:
            print('Такого канала не существует!')
        flag = False
    print('Ваши избранные каналы:', favorite_lst)


add_to_favorite()
