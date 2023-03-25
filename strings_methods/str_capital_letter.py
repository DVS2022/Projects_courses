def capital_letter():
    """ Capitalizes every word in a sentence. """
    text = input('Введите предложение: ').split()
    text_lst = []
    for i in text:
        text_lst.append(i.capitalize())
    text_lst = ' '.join(text_lst)
    print(text_lst)


capital_letter()
