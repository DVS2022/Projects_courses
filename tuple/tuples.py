import random


def tuples():
    """ Generates random tuples, concatenates them, counts the zeros,
    and prints the tuples and the count."""
    t1 = tuple(random.randint(0, 5) for _ in range(10))
    t2 = tuple(random.randint(0, 5) for _ in range(5))
    t3 = t1 + t2
    count_zeros = t3.count(0)
    print('First tuple:', t1)
    print('Second tuple:', t2)
    print('Tuple after union:', t3)
    print('Count zeros in union tuple:', count_zeros)


tuples()
