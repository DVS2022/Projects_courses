def bubble_sort():
    lst = [5, 3, 7, 9, -3, -10, 1, 4, 6, -4]
    print('Изначальный список: ', lst)
    for i in range(len(lst)):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                print(lst)
    print('Отсортированный список: ', lst)


bubble_sort()
