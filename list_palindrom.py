def palindrome():
    """ Функция проверяет, является ли слово палиндромом """
    word = str(input('Введите слово: '))
    reverse_word = word[::-1]
    if word == reverse_word:
        print('Слово является палиндромом!')
    else:
        print('Слово не является палиндромом!')
    print(word, '\n', reverse_word, sep='')


palindrome()
