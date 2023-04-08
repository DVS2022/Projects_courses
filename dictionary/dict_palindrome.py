def can_be_palindrome(string_1):
    """ Checks if a string can be made a palindrome. """
    char_count = {}
    for c in string_1:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    odd_count = 0
    for count in char_count.values():
        if count % 2 == 1:
            odd_count += 1
        if odd_count > 1:
            return False
    return True


string = input("Enter string: ")
if can_be_palindrome(string):
    print("Can be made a palindrome")
else:
    print("Can't be a palindrome")
