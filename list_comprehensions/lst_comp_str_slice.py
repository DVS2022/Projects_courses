def str_slice():
    """ Applies a slice using various methods to a string. """
    word = str(input('Введите слово: '))
    print('Копия:', word[:])
    print('Обратный порядок:', word[::-1])
    print('Каждый второй элемент:', word[::2])
    print('Каждый второй элемент со 2:', word[1::2])
    print('Все элементы кроме последних 3:', word[:-3:])
    print('Все элементы от 3 до 4 (включительно):', word[3:5:])
    print('Последние 5 элементов строки:', word[-5:])
    print('Все элементы от 3 до 4 (включительно) в обратном порядке:',
          word[4:2:-1])


str_slice()
