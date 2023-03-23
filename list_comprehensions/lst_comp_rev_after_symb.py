def reverse_after_symbol():
    """ Revers the string between the first character "!" and last. """
    string = '0123!456!789!10'
    first_h_index = string.find('!')
    last_h_index = string.rfind('!')
    substring = string[first_h_index + 1:last_h_index]
    reversed_substring = substring[::-1]
    print(string[:first_h_index + 1] + reversed_substring +
          string[last_h_index:])


reverse_after_symbol()
