def summ_numbers(number):
    """ Функция принимает одно целое положительное число и находит
    сумму всех цифр этого числа. """
    summ = 0
    while number != 0:
        digit = number % 10
        summ += digit
        number //= 10
    return summ


def count_digits(number):
    """ Функция считает количество цифр в числе. """
    count = 0
    while number != 0:
        count += 1
        number //= 10
    return count


n = int(input('Введите целое положительное число: '))
total_summ = summ_numbers(n)
total_count = count_digits(n)
result = total_summ - total_count
print('Сумма чисел:', total_summ)
print('Количество цифр в числе:', total_count)
print('Разность суммы чисел и количества цифр:', result)
