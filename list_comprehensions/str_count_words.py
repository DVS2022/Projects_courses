def count_words():
    """ Counts the number of 3 specific words found in the text. """
    lst = []
    for i in range(3):
        word = str(input(f'Введите {i+1} слово для поиска: '))
        lst.append(word)
    text = input('Введите текст: ').lower().split()
    for j in range(3):
        print(lst[j], ':', text.count(lst[j]))


count_words()
