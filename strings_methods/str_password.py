def password():
    """ Standard password protection check. """
    flag = False
    flag_end = True
    count = 0
    while flag_end:
        str_password = input('Введите пароль: ')
        if len(str_password) >= 8:
            count = 0
            for i in str_password:
                if i.isupper() is True:
                    flag = True
                elif i.isnumeric():
                    count += 1
        else:
            print('Пароль должен быть не менее 8 символов!')
        if count > 2 and flag:
            print('Пароль подходит по надежности!')
            flag_end = False
        else:
            print('В пароле должны присутствовать минимум 3 цифры и заглавная буква')


password()
