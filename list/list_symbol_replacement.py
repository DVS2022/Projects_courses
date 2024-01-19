def sym_replace():
    """ Функция принимает текст пользователя, заменяет
    в списке все точки на запятые и подсчитывает кол-во замен """
    text = list(input('Введите строку с точками: '))
    count = 0
    for i in range(len(text)):
        if text[i] == '.':
            text[i] = ','
            count += 1
    print('Исправленный текст:', end=' ')
    for i in text:
        print(i, end='')
    print('\nЗаменено точек:', count)


sym_replace()
