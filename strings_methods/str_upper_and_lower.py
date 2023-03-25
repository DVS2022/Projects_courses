def upper_and_lower():
    """ Checks if there are more uppercase letters in the string,
    makes all letters large, otherwise small.
    """
    string = str(input('Введите строку: '))
    up_lst = string.split()
    up = ' '.join(up_lst)
    count = 0
    for i in range(len(up)):
        if up[i].isupper():
            count += 1
    if len(string) / count < 2:
        string = string.upper()
    elif len(string) / count > 2:
        string = string.lower()
    print(string)


upper_and_lower()
