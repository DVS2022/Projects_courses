def ip_address():
    """ Multi-factor IP address check. """
    ip_str = input('Введите ip-адрес: ').split('.')
    count = 0
    if len(ip_str) != 4:
        print('Неверный формат адреса!')
        return
    for i in range(4):
        if not ip_str[i].isnumeric():
            print(ip_str[i], '- не целое число!')
        elif 0 <= int(ip_str[i]) <= 255:
            count += 1
        else:
            print(f'Ошибка ввода! Число {ip_str[i]} должно быть от 0 до 225')
            break
    if count == 4:
        print('Ваш ip-адрес корректен.')


ip_address()
