def negative_to_zero():
    """ From the given list makes another one in
    which negative values are replaced by 0.
    """
    lst = [10, -20, -30, 40, 50, -60]
    new_lst = [(0 if x < 0 else x) for x in lst]
    print(new_lst)


negative_to_zero()
