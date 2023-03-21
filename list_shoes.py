def shoes():
    """ Функция составляет два списка и сравнивает их значения, если
        значение из первого списка равно или больше, чем значение второго,
        счетчик увеличивается на 1. """
    amount_numbers_1 = int(input('Введите количество чисел в списке №1: '))
    lst_1 = []
    lst_2 = []
    for i in range(amount_numbers_1):
        lst_1.append(int(input(f'Введите {i + 1} число добавляемое '
                                    f'в список №1: ')))
    amount_numbers_2 = int(input('Введите количество чисел в списке №1: '))
    for i in range(amount_numbers_2):
        lst_2.append(int(input(f'Введите {i + 1} число добавляемое '
                                    f'в список №2: ')))
    lst_1.sort()
    lst_2.sort()
    print(lst_1)
    print(lst_2)
    count = 0
    for i in range(len(lst_1)):
        for j in range(len(lst_2)):
            if lst_2[j] == lst_1[i] and lst_1[i] != 0:
                count += 1
                lst_1[i] = 0
                lst_2[j] = 1
            elif lst_2[j] < lst_1[i] and lst_2[j] != 1:
                count += 1
                lst_1[i] = 0
                lst_2[j] = 1
    print(lst_1)
    print(lst_2)
    print(count)


shoes()
