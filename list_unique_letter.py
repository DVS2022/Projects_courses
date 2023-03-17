def unique_letter():
    """ Функция подсчитывает количество уникальных букв в слове. """
    word = list(input('Введите слово: '))
    count_1 = 0
    count_all = 0
    for i in range(len(word)):
        letter = word[i]
        for j in range(len(word)):
            if letter == word[j]:
                count_1 += 1
        if count_1 == 1:
            count_all += 1
        count_1 = 0
    print('Уникальных букв в слове: ', count_all)


unique_letter()
