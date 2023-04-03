def multi_get():
    """ Extracts data from the given structure. """
    family_member = {
        'name': 'Наталия',
        'surname': 'Дёмочкина',
        'hobbies': ['чтение, плавание'],
        'age': 34,
        'children': [
            {
                'name': 'Александр',
                'age': 7
            },
            {
                'name': 'Максим',
                'age': 5
            }
        ]
    }
    children = family_member.get('children', [])
    search_name = input('Введите имя ребенка: ')
    flag = False
    for i in children:
        if i['name'] == search_name:
            print('Есть такой ребенок!')
            flag = True
    if not flag:
        print('Нет такого ребенка!')


multi_get()
