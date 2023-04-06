def api():
    """ Defines a dictionary called data that contains nested
    dictionaries and lists. The function then prints the keys
    and values of the data dictionary, modifies some of its
    values, and prints the updated dictionary.
    """
    data = {
        'address': 'hh123456789',
        'TTT': {
            'balance': 123,
            'total_in': 123,
            'total_out': 5
        },
        'count_txs': 3,
        'tokens': [
            {
                'fst_token_info': {
                    'address': 'hh987654321',
                    'name': 'fst_token',
                    'decimals': '1',
                    'symbol': 'FT',
                    'total_supply': '322',
                    'owner': 'Albert',
                    'last_updated': 112233445566778899,
                    'issuances_count': 0,
                    'holders_count': 10000,
                    'price': False
                },
                'balance': 300,
                'total_in': 2,
                'total_out': 2
            },
            {
                'sec_token_info': {
                    'address': 'hh123321123',
                    'name': 'sec_token',
                    'decimals': '2',
                    'symbol': 'ST',
                    'total_supply': '218218',
                    'owner': 'neAlbert',
                    'last_updated': 321321321,
                    'issuances_count': 0,
                    'holders_count': 20000,
                    'price': False
                },
                'balance': 1000,
                'total_in': 1,
                'total_out': 1
            }
        ]
    }

    print('Списки ключей и значений словаря:')
    for key, value in data.items():
        print(key, ':', value)

    data['TTT']['total_diff'] = 555

    data['tokens'][0]['fst_token_info']['name'] = 'Aleksei'

    total_out = data['tokens'][0].pop('total_out')
    data['TTT']['total_out'] = total_out

    data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')

    print('Измененный словарь:', data)


api()
