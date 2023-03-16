def odd():
    """ Функция генерирует список от 1 до N из нечетных чисел """
    amount = int(input('Введите целое число: '))
    list1 = []
    for i in range(1, amount+1, 2):
        list1.append(i)
    print('Список нечетных чисел:', list1)


odd()
