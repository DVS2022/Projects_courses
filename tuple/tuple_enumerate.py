def show_index(my_tuple):
    """ Takes a string (some_str) as an argument. The function iterates
    over the characters in the string using enumerate and checks if a
    character is equal to '~'. If a '~' is found, the index of that character
    is added to a tuple (my_tuple). The resulting tuple of indices is then returned.
    """
    my_tuple = ()
    for i_str, i_value in enumerate(some_str):
        if i_value == '~':
            my_tuple += (i_str,)
    return my_tuple


some_str = 'so~mec~od~e'
numbers = show_index(some_str)
print('Indexes of "~" :', *numbers)
