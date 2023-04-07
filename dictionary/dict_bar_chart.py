def bar_chart():
    """ Takes user input for a string of text and creates a bar
    chart displaying the frequency of each symbol (character) in
    the text and shows max frequency.
    """
    text = input('Введите текст: ').lower()
    symbol_dict = dict()
    for symbol in text:
        if symbol in symbol_dict:
            symbol_dict[symbol] += 1
        else:
            symbol_dict[symbol] = 1
    for i_sym in sorted(symbol_dict.keys()):
        print(i_sym, '-', symbol_dict[i_sym])
    print('Наибольшая частота:', max(symbol_dict.values()))


bar_chart()
