def specific_place():
    """ Функция получает последовательность из убывающих чисел и число N.
    Вставляет это число N в необходимый промежуток """
    amount = int(input('Введите количество чисел: '))
    lst = []
    for i in range(amount):
        number = int(input(f'Введите число №{i+1}: '))
        lst.append(number)
    new = int(input('Введите новое число: '))
    lst.append(0)
    for i in range(len(lst)):
        if new > lst[i]:
            print('Номер куда стоит вставить новое число:', i+1)
            break


specific_place()
