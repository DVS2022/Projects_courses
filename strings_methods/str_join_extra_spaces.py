def join_extra_spaces():
    """ Removes extra spaces in text. """
    text = str(input('Введите текст (с лишними пробелами): ')).split()
    new_text = ' '.join(text)
    print(new_text)


join_extra_spaces()
