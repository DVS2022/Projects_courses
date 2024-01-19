import math


def cylinder():
    """ Takes the radius and height of the cylinder, calculates
    the surface area of its side and the total area of this cylinder.
    """
    radius = int(input('Enter the radius of the cylinder: '))
    height = int(input('Enter the height of the cylinder: '))
    side_area = 2 * math.pi * radius * height
    full_area = side_area + 2 * (math.pi * radius ** 2)
    return side_area, full_area


side_area_1, full_area_1 = cylinder()
print('Side area of the cylinder -', side_area_1)
print('Full area of the cylinder -', full_area_1)
