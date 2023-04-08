def guess_number():
    """ A simple number guessing game. """
    n = int(input("Enter maximum number: "))
    possible_numbers = set(range(1, n + 1))
    while True:
        numbers_str = input("The required number is among these numbers: ")
        if numbers_str == "Help!":
            print("Hidden numbers:", *possible_numbers)
            break
        numbers = set(map(int, numbers_str.split()))
        answer = input('Enter the answer is there any hidden among '
                       'these numbers (Yes/No): ')
        if answer == 'Yes':
            possible_numbers &= numbers
        elif answer == 'No':
            possible_numbers -= numbers
        else:
            print('Input Error!')


guess_number()
