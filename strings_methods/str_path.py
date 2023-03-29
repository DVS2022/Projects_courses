def check_path():
    """ Checks file path (drive and extension). """
    path = str(input('Введите путь к файлу: '))
    start = str(input('На каком диске файл?: '))
    end = str(input('Расширение файла?: '))
    start = path.startswith(start)
    end = path.endswith(end)
    if not start:
        print('Диск не совпадает!')
    elif not end:
        print('Расширение не совпадает!')
    else:
        print('Всё ок!')


check_path()
