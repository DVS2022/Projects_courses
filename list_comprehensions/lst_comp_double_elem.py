def double_element():
    """ Constructs a list from a string, tripling the number of
    elements and adding any character needed.
    """
    string = str(input('Введите строку: '))
    symbol = str(input('Введите символ: '))
    result = [x*3+symbol for x in string]
    print(result)


double_element()
