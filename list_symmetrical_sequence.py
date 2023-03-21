def is_palindrome(lst):
    """ Функция проверяет, является ли последовательность симметричной,
    если нет, то добавляет в новый список последний элемент и возвращает False. """
    reverse_list = []
    for i in range(len(lst) - 1, -1, -1):
        reverse_list.append(lst[i])
    if lst == reverse_list:
        return True
    else:
        return False


def symmetrical_sequence():
    """ Функция принимает цифры для создания последовательности и
    передает данные в is_palindrome(). Выдает список цифр для
    составления симметричной последовательности. """
    amount_numbers = int(input('Введите количество чисел: '))
    lst = []
    for i in range(amount_numbers):
        number = int(input('Введите число: '))
        lst.append(number)
    new_lst = []
    answer = []
    for i in range(0, len(lst)):
        for j in range(i, len(lst)):
            new_lst.append(lst[j])
        if is_palindrome(new_lst):
            for i in range(0, i):
                answer.append(lst[i])
            answer.reverse()
            break
        new_lst = []
    print('Изначальный список: ', lst)
    print('Нужно чисел для симметрической последовательности: ', len(answer))
    print('Конечный список для добавления: ', answer)


symmetrical_sequence()
