def control():
    """ Функция создает список ID сотрудников и проверяет, присутствует ли конкретный работник на рабочем месте. """
    number_of_people = int(input('Введите количество сотрудников: '))
    ids = []
    flag = False
    for i in range(number_of_people):
        id_employee = int(input('Введите ID сотрудника: '))
        ids.append(id_employee)
    desired_employee = int(input('Введите ID искомого сотрудника: '))
    for curr_id in ids:
        if curr_id == desired_employee:
            flag = True
    if not flag:
        print('Сотрудник отсутствует!')
    else:
        print('Сотрудник на рабочем месте')


control()
