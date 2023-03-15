def reverse_int(x):
    """ Функция выделяет и разворачивает целую часть натурального числа"""
    integer_part = int(x)
    integer_part_reversed = 0
    while integer_part > 0:
        integer_part_reversed = integer_part_reversed * 10 + integer_part % 10
        integer_part = integer_part // 10
    return integer_part_reversed


def reverse_fractional(number):
    """ Функция выделяет и разворачивает дробную часть натурального числа"""
    fraction = number - int(number)
    fraction = round(fraction, 10)
    reversed_fraction = 0
    count = 0
    while fraction > 0:
        fraction *= 10
        digit = int(fraction % 10)
        reversed_fraction = round(reversed_fraction * 10 + digit, 7)
        fraction = round(fraction - digit, 7)
        count += 1
    result = reverse_int(reversed_fraction) / 10**count
    return result


number1 = float(input('Введите первое натуральное число: '))
number2 = float(input('Введите второе натуральное число: '))
reversed_int_1 = reverse_int(number1)
reversed_fractional_1 = reverse_fractional(number1)
reversed_int_2 = reverse_int(number2)
reversed_fractional_2 = reverse_fractional(number2)
reversed_1 = reversed_int_1 + reversed_fractional_1
reversed_2 = reversed_int_2 + reversed_fractional_2
print('Первое число наоборот:', reversed_1)
print('Второе число наоборот:', reversed_2)
print('Сумма чисел:', reversed_1 + reversed_2)
