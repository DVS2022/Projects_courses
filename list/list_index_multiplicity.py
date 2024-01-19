def index_multiplicity():
    """ Функция создает список целых чисел, из них находит кратные определенному
     числу К и складывает индексы этих чисел"""
    amount_of_numbers = int(input('Введите количество чисел: '))
    list_1 = []
    summ = 0
    for i in range(amount_of_numbers):
        number = int(input(f'Введите {i + 1} число: '))
        list_1.append(number)
    k = int(input('Введите делитель: '))
    for i_numb in range(amount_of_numbers):
        if (list_1[i_numb] % k) == 0:
            print(f'Индекс числа {list_1[i_numb]}: {i_numb}')
            summ += i_numb
    print('Сумма кратных индексов:', summ)


index_multiplicity()
