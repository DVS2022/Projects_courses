def encoding():
    """ Reads a string, groups of identical characters of the source
    string are replaced with this character and the number of
    repetitions of it in this position of the string.
    """
    text = input('Введите текст: ')
    encoded_text = ''
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            encoded_text += text[i-1] + str(count)
            count = 1

    encoded_text += text[-1] + str(count)
    print('Кодированный текст: ', encoded_text)


encoding()
