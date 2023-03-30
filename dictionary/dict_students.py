def students():
    """ Receives data and makes a dictionary out of them. """
    lst = input('Введите данные студента через пробел '
                '(фамилию, имя, город, вуз и все оценки): ').split()
    student_info = dict()
    student_info['Имя'] = lst[0]
    student_info['Фамилия'] = lst[1]
    student_info['Город'] = lst[2]
    student_info['ВУЗ'] = lst[3]
    student_info['Оценки'] = []
    for i in lst[4:]:
        student_info['Оценки'].append(int(i))
    for j in student_info:
        print(j, '-', student_info[j])


students()
