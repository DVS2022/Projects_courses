def bit_packets():
    """ Функция проверяет целостность пакетов битовой информации. """
    amount = int(input('Введите количество пакетов: '))
    massage = []
    count_bad_pack = 0
    for i in range(amount):
        pack_lst = []
        flag = False
        count = 0
        print(f'Пакет №{i + 1}')
        for j in range(4):
            bit = int(input(f'Введите бит №{j+1}: '))
            pack_lst.append(bit)
            if bit == -1:
                count += 1
            elif bit != 1 and bit != 0:
                print('Ошибка! Неверные данные')
                flag = True
                break
            if count >= 2:
                flag = True
        if not flag:
            massage.extend(pack_lst)
        else:
            print('Больше 1й ошибки в пакете. Пакет заблокирован!')
            count_bad_pack += 1
    print('Полученное сервером сообщение: ', massage)
    print('Количество ошибок в сообщении: ', massage.count(-1))
    print('Количество потерянных пакетов: ', count_bad_pack)


bit_packets()
