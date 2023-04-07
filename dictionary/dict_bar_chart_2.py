def bar_chart_2():
    """ Takes user input for a string of text and creates a bar
    chart displaying the frequency of each symbol (character) in
    the text.
    """
    text = input('Введите текст: ').lower()
    symbol_dict = dict()
    for symbol in text:
        if symbol in symbol_dict:
            symbol_dict[symbol] += 1
        else:
            symbol_dict[symbol] = 1
    print('Оригинальный словарь: ')
    for i_sym in sorted(symbol_dict.keys()):
        print(i_sym, '-', symbol_dict[i_sym])
    inverse_dict = invert_dict(symbol_dict)
    print('Инвертированный словарь:')
    for count, symbols in sorted(inverse_dict.items()):
        print(count, '-', symbols)


def invert_dict(dict_1):
    """ Iterates over the keys and values of the dictionary, and for
    each value creates a new element of the inverse_dict dictionary,
    in which the key is the frequency of characters, and the value is
    a list of characters with that frequency. If the inverse_dict
    dictionary already contains such a key, then the function adds the
    current character to the list for that frequency.
    """
    inverse_dict = dict()
    for key, value in dict_1.items():
        if value in inverse_dict:
            inverse_dict[value].append(key)
        else:
            inverse_dict[value] = [key]
    return inverse_dict


bar_chart_2()
