def is_number():
    """ Gets text with numbers and separates the numbers into
    a separate line.
    """
    text = str(input('Введите текст с цифрами: '))
    num_lst = []
    for i in text:
        if i.isnumeric():
            num_lst.append(str(i))
    num_text = ''.join(num_lst)
    print('Строка цифр:', num_text)


is_number()
