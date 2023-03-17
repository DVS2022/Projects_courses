def del_max():
    """ Функция принимает список чисел и удаляет наибольший элемент списка """
    amount = int(input('Введите количество чисел: '))
    list_1 = []
    max_index = 0
    for i in range(amount):
        print(i+1, 'Элемент ', end='')
        number = int(input(''))
        list_1.append(number)
    max_num = list_1[0]
    for i in range(len(list_1)):
        if list_1[i] > max_num:
            max_num = list_1[i]
            max_index = i
    list_new = []
    for i in range(len(list_1)):
        if i != max_index and list_1[i] != max_num:
            list_new.append(list_1[i])
    print('Изначальный список:', list_1)
    print('Измененный список:', list_new)


del_max()
