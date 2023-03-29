def annoying_reminder():
    """ Reminds the debtor of debt in an annoying way. """
    name = str(input('Введите имя: '))
    debt = str(input('Введите сумму долга: '))
    print('{0}, привет! Привет, {0}! Как дела, {0}? Где мои {1}'
          ' батов, {0}?'.format(
            name,
            debt
            ))


annoying_reminder()
