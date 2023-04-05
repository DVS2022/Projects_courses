def numbers_in_string():
    """ Finds all distinct digits in a character string. """
    text = input('Введите строку: ')
    nums = set()
    for i in text:
        if '0' <= i <= '9':
            nums.add(i)
    print('Цифры встречающиеся в строке:', end=' ')
    for j in nums:
        print(j, end=', ')


numbers_in_string()
