def min_max():
    """ Функция для поиска минимального и максимального числа в списке. """
    nums_list = []
    n = int(input('Кол-во чисел в списке: '))
    for i in range(n):
        num = int(input('Введите очередное число: '))
        nums_list.append(num)
    maximum = nums_list[0]
    minimum = nums_list[0]
    for i in nums_list:
        if maximum < i:
            maximum = i
        if minimum > i:
            minimum = i
    print('Минимальное число в списке:', minimum)
    print('Максимальное число в списке:', maximum)


min_max()
