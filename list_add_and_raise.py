def add_and_raise():
    """ Функция добавляет элемент в двумерный список и увеличивает
    стоимость всех блюд на 10%. """
    lst = [['Первое', 100], ['Второе', 150], ['Компот', 20], ['Десерт', 50]]
    new_dish = str(input('Введите новое блюдо: '))
    new_price = int(input('Введите цену этого блюда: '))
    lst_new_dish = [new_dish, new_price]
    lst.append(lst_new_dish)
    print('Список блюд:', lst)
    for i in range(len(lst)):
        lst[i][1] += lst[i][1] * 0.1
    print('Список блюд после добавления 10%:', lst)


add_and_raise()
