def symbol_pos_compare():
    """ Функция принимает строку, запрашивает номер позиции символа,
    выводит соседние символы и сравнивает их"""
    text = list(input('Введите текст: '))
    symbol_index = int(input('Введите номер символа: '))
    for i in range(len(text)):
        if i == symbol_index-1:
            print(f'Символ слева: {text[i-1]}\nСимвол справа: {text[i+1]}')
            if text[i-1] == text[i] and text[i] == text[i+1]:
                print('Рядом два таких же символа')
                break
            elif text[i-1] == text[i] or text[i] == text[i+1]:
                print('Рядом один такой же символ')
                break
            else:
                print('Рядом такие же символы отсутствуют')


symbol_pos_compare()
