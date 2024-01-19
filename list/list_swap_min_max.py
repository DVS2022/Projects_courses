def swap():
    """ Функция создает список из n-элементов и меняет местами минимум и максимум """
    nums_list = []
    amount = int(input('Введите количество чисел: '))
    for i in range(amount):
        number = int(input(f'Введите {i+1} число: '))
        nums_list.append(number)
    print('Введённый список:', nums_list)
    maximum = nums_list[0]
    minimum = nums_list[0]
    index_min = 0
    index_max = 0
    for i_numb in range(amount):
        if nums_list[i_numb] < minimum:
            minimum = nums_list[i_numb]
            index_min = i_numb
        elif nums_list[i_numb] > maximum:
            maximum = nums_list[i_numb]
            index_max = i_numb
    nums_list[index_min], nums_list[index_max] = nums_list[index_max], nums_list[index_min]
    print('Список после смены минимума с максимумом:', nums_list)


swap()
