def longest_word():
    """ Finds the longest word in a string and counts its length. """
    string = str(input('Введите слова через пробел: ')).split()
    longest = 0
    for i in range(len(string)):
        if len(string[i]) > len(str(longest)):
            longest = string[i]
    print('Самое длинное слово:', longest)
    print('Количество букв:', len(longest))


longest_word()
