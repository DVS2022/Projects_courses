def count_symbols():
    """ Accepts text, counts punctuation marks from a set. """
    text = input('Введите текст: ')
    symbols = {'.', ',', ':', ';', '!', '?'}
    count = 0
    for i in text:
        if i in symbols:
            count += 1
    print('Количество знаков пунктуации:', count)


count_symbols()
