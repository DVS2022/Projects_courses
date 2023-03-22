def count_vowels():
    """ Takes text, finds vowels in it, makes a list of vowels
    and counts their number.
    """
    text = input('Введите текст: ')
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    result = [letter for letter in text if letter in vowels]
    print('Список гласных букв:', result)
    print('Количество гласных:', len(result))


count_vowels()
