def caesar_cipher():
    """ Encrypts a message in Russian with a Caesar cipher.
    Text and offset are user input.
    """
    text = str(input('Введите текст для шифрования: '))
    shift = int(input('Введите сдвиг: '))
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    encrypted = ''.join([alphabet[(alphabet.index(char) + shift) %
                        len(alphabet)] if char in
                        alphabet else char for char in text])
    print('Шифр:', encrypted)


caesar_cipher()
