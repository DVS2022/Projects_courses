import random
import string


def random_list():
    """ Generates a list containing 10 randomly chosen lowercase letters. """
    random_letters = [random.choice(string.ascii_lowercase) for _ in range(10)]
    return random_letters


def make_dict(rand_lst):
    """ Takes a sequence 'rand_lst' as input, iterates through its elements
    using enumerate, and creates a tuple for each element consisting of its
    index and value. These tuples are then appended to some_tuple. Finally,
    the function converts some_tuple into a dictionary using dict()
    """
    some_tuple = ()
    for i, value in enumerate(rand_lst):
        i_tuple = (i, value)
        some_tuple += (i_tuple,)
    result_dict = dict(some_tuple)
    return result_dict


list_1 = random_list()
list_2 = random_list()
print(list_1)
print(list_2)
print(make_dict(list_1))
print(make_dict(list_2))
