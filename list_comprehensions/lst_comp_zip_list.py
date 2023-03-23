def zip_list():
    """ Rearrange all non-zero elements to the beginning and
    remove all zeros from the list.
    """
    lst = [0, 1, 2, 0, 3, 4, 0, 5, 6, 7, 0, 0, 8, 9]
    print(lst)
    count = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[count], lst[i] = lst[i], lst[count]
            count += 1
    print(lst)
    lst = lst[:count]
    print(lst)


zip_list()
