def cities():
    """ Reads the number of countries and then prompts the user to
    enter the name of each country followed by its cities on the same
    line. Stores this information in a dictionary where the keys are
    the city names and the values are the country names. After that
    the user enter the names of three cities and checks if each city
    is in the dictionary.
    """
    amount = int(input('Введите количество стран: '))
    countries = dict()
    for i in range(amount):
        data = input(f'Введите страну под № {i+1} и '
                     f'3 города в ней через пробел: ').split()
        country = data[0]
        cities_1 = data[1:]
        for city in cities_1:
            countries[city] = country

    for j in range(3):
        city = input(f'Введите {j+1} город для поиска: ')
        if city in countries:
            print(f'{city} находится в стране {countries[city]}.')
        else:
            print('Данного города нет в списках!')


cities()
