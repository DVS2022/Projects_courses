def correct_input():
    """ Checks the correctness of the input file name. """
    string = str(input('Введите название файла: '))
    if string.startswith(('\\', '|', '/', '@', '№', '$', '%', '^', '&', '*', '(', ')')):
        print('Недопустимый первый символ файла!')
    elif not string.endswith(('.exe', '.jpg', '.jpeg')):
        print('Неверное расширение файла!')
    else:
        print('Всё ок!')


correct_input()
