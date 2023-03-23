def two_dimensional_list():
    """ Creates a two-dimensional list. """
    lst = [[i for i in range(1, 17, 5)], [j for j in range(2, 18, 5)],
           [x for x in range(3, 19, 5)], [y for y in range(4, 20, 5)]
           ]
    print(lst)


two_dimensional_list()
