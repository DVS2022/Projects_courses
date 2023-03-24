import random


def game_sticks():
    """ A game in which you enter the number of sticks and the number of throws on them.
    Sticks are randomly knocked down in a certain interval. At the end, the result of the
    vertical and horizontal sticks is displayed.
    """
    amount_sticks = int(input('Введите количество палочек: '))
    amount_throws = int(input('Введите количество бросков: '))
    lst = ['|' for _ in range(amount_sticks)]
    score = ''
    for i in range(amount_throws):
        start, stop = random.randint(1, amount_sticks), random.randint(1, amount_sticks)
        if start > stop:
            start, stop = stop, start
        break_range = range(start-1, stop)
        print(f'Бросок №{i+1} Были сбиты палочки №№ {start}-{stop}')
        lst = ['_' if j in break_range else lst[j] for j in
               range(amount_sticks)]
        print(score.join(lst))
        print()


game_sticks()
