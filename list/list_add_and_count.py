def add_and_count():
    """ Функция добавляет элементы из одного списка в другой и подсчитывает их стоимость. """
    lst = [['Первый', 1.5], ['Второй', 2.5], ['Третий', 3.5], ['Четвертый', 4.5], ['Пятый', 5.5],
           ['Шестой', 6.5], ['Седьмой', 7.5], ['Восьмой', 8.5], ['Девятый', 9.5], ['Десятый', 10.1],
           ]
    lst_my = []
    summ = 0
    number = int(input('Введите количество элементов списка: '))
    for i in range(number):
        name = str(input(f'Введите имя элемента {i+1}: '))
        flag = False
        for i_name in range(len(lst)):
            if lst[i_name][0] == name:
                lst_my.append(name)
                summ += lst[i_name][1]
                flag = True
        if not flag:
            print('Нет элемента в списке!')
    print(f'Итого список: {lst_my}, с общей стоимостью: {summ}')


add_and_count()
