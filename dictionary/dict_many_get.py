def many_get():
    players_dict = {
        1: {'name': 'Вадим', 'team': 'A', 'status': 'Работает'},
        2: {'name': 'Александр', 'team': 'B', 'status': 'Отдыхает'},
        3: {'name': 'Наталия', 'team': 'C', 'status': 'Отсутствует'},
        4: {'name': 'Максим', 'team': 'A', 'status': 'Работает'},
        5: {'name': 'Ольга', 'team': 'B', 'status': 'Отдыхает'},
        6: {'name': 'Сергей', 'team': 'C', 'status': 'Отсутствует'},
        7: {'name': 'Галина', 'team': 'A', 'status': 'Отдыхает'},
        8: {'name': 'Дмитрий', 'team': 'B', 'status': 'Отсутствует'},
        9: {'name': 'Анастасия', 'team': 'C', 'status': 'Работает'}
    }

    team_a_workers = [
        player['name']
        for player in players_dict.values()
        if player['team'] == 'A' and player['status'] == 'Работает'
        ]
    print(team_a_workers)

    team_b_rest = [
        player['name']
        for player in players_dict.values()
        if player['team'] == 'B' and player['status'] == 'Отдыхает'
        ]
    print(team_b_rest)

    team_c_absent = [
        player['name']
        for player in players_dict.values()
        if player['team'] == 'C' and player['status'] == 'Отсутствует'
        ]
    print(team_c_absent)


many_get()
