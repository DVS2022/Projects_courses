def coordinates():
    """ Accepts coordinates, displays them in a different format. """
    coord = []
    for i in range(2):
        coord_1 = input('Введите координаты (С, Ю, З, В и число '
                        'через пробел): ').split()
        coord.insert(i, coord_1)
    cardinal_directions = [['С', '+'], ['Ю', '-'], ['З', '-'], ['В', '+']]
    result = []
    count = 0
    for i in range(len(coord)):
        for j in range(len(cardinal_directions)):
            if coord[i][0] == cardinal_directions[j][0]:
                result.append(cardinal_directions[j][1])
                result.append(coord[i][1])
                result.append(' ')
                count += 1
    if count <= 1:
        print('Нет таких координат')
    else:
        print('Координаты (X, Y):', ''.join(result))


coordinates()
