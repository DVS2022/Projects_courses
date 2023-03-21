def input_and_unique():
    """ Функция принимает значения двух списков, объединяет их и делает
    значения уникальными. """
    number_first = int(input('Введите количество чисел в списке №1: '))
    number_second = int(input('Введите количество чисел в списке №2: '))
    list_first = []
    list_second = []
    for i in range(number_first):
        list_first.append(int(input(f'Введите {i+1} число добавляемое '
                                    f'в список №1: ')))
    for i in range(number_second):
        list_second.append(int(input(f'Введите {i+1} число добавляемое '
                                     f'в список №2: ')))
    print('Первый список:', list_first)
    print('Второй список:', list_second)
    list_first.extend(list_second)
    unique_numbers = list(set(list_first))
    print('Уникальные значения после объединения:', unique_numbers)


input_and_unique()
