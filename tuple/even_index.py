def get_even_index(some_arg):
    """ Takes a string, list, dictionary, or tuple as an argument. It
    returns a new list containing elements from the input located at
    even indices. If the input is not of the expected types, it prints
    an error message.
    """
    if isinstance(some_arg, (str, list, dict, tuple)):
        this_list = []
        for i, value in enumerate(some_arg):
            if i % 2 == 0:
                this_list.append(value)
        return this_list
    else:
        print('Неверный тип данных', end=' ')


some_str = 123
some_lst = [1, 2, 3, 'бук', '$', 2, 'Y']

print(get_even_index(some_str))
print(get_even_index(some_lst))
