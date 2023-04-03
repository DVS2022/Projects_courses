import random


def sets():
    """ Generates two sets of random numbers, removes their minimum
    value, adds a random number between 20 and 30 to each set, and
    then performs several set operations on them. The function then
    prints the resulting sets and outputs some information about them.
    """
    nums_1 = [random.randint(1, 20) for x in range(20)]
    nums_2 = [random.randint(1, 20) for x in range(20)]
    print(nums_1)
    print(nums_2)

    set_1 = set(nums_1)
    set_2 = set(nums_2)

    set_1.remove(min(set_1))
    set_2.remove(min(set_2))
    set_1.add(random.randint(20, 30))
    set_2.add(random.randint(20, 30))

    print("1-е множество:", set_1)
    print("2-е множество:", set_2)
    print("Пересечение множеств:", set_1.intersection(set_2))
    print("Элементы, входящие в nums_2, но не входящие в nums_1:", set_2.difference(set_1))
    print("Минимальный элемент 1-го множества:", min(set_1))
    print("Минимальный элемент 2-го множества:", min(set_2))
    print("Случайное число из 1-го множества:", random.choice(tuple(set_1)))
    print("Случайное число из 2-го множества:", random.choice(tuple(set_2)))


sets()
