def management():
    """ Функция получает количество сотрудников, также их зарплаты,
    (ввод 0 означает что сотрудник уволен). Выводит список зарплат,
    показывает минимальную и максимальную зарплату. """
    number_of_employees = int(input('Введите количество сотрудников: '))
    count = 0
    lst = []
    for i in range(number_of_employees):
        salary = int(input(f'Укажите зарплату сотрудника №{i+1}: '))
        if salary != 0:
            count += 1
            lst.append(salary)
    print('Всего сотрудников на зарплате:', count)
    print('Список зарплат:', lst)
    print('Минимальная зп:', min(lst))
    print('Максимальная зп:', max(lst))


management()
