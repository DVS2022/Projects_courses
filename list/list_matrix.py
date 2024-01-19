def matrix():
    matrix_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i_row in matrix_lst:
        for row in i_row:
            print(row, end=' ')
        print()


matrix()
