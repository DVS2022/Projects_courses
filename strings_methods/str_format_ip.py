def ip_address():
    """ Takes 4 numbers as input and displays an IP address. """
    ip_str = ''
    for i in range(4):
        number = int(input('Введите {0} номер ip адреса: '.format(i+1)))
        if 0 <= number <= 225:
            ip_str += str(number)
            if i != 3:
                ip_str += '.'
        else:
            print('Ошибка ввода! Число должно быть от 0 до 225')
            break
    print('Ваш ip-адрес:', ip_str)


ip_address()
