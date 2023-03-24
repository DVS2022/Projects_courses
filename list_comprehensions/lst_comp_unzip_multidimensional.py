def unzip_lst():
    """ Unpacks a multidimensional list. """
    lst = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
        ]
    unzipped_lst = [element for sub_list in lst for sub_sub_list in
                    sub_list for element in sub_sub_list]
    print(unzipped_lst)


unzip_lst()
