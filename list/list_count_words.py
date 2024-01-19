def count_words():
    """ Функция принимает 3 слова и текст по словам, затем считает
    сколько и какое слово встречается в тексте """
    words_list = []
    counts = [0, 0, 0]
    for i in range(3):
        print('Введите', i + 1, 'слово:', end=' ')
        word = input()
        words_list.append(word)
    text = input('Введите слово из текста: ')
    while text != 'end':
        for i in range(3):
            if words_list[i] == text:
                counts[i] += 1
        text = input('Введите слово из текста: ')
    print('\nПодсчитываем слова в тексте...')
    for i in range(3):
        print(f'{words_list[i]}: {counts[i]} шт.')


count_words()
