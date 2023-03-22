import random


def list_generate_and_compare():
    """ Generates two lists with real numbers, combines them according
    to the principle of large values.
    """
    lst_1 = [round(random.uniform(0, 10.00), 2) for _ in range(20)]
    lst_2 = [round(random.uniform(0, 10.00), 2) for _ in range(20)]
    lst_compare = [lst_1[i] if lst_1[i] > lst_2[i] else
                   lst_2[i] for i in range(len(lst_1))]
    print(lst_1)
    print(lst_2)
    print(lst_compare)


list_generate_and_compare()
