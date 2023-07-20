cidade = str(input('Informe o nome da sua cidade:  '))
print('A tua palavra começa com santos?\n{}'.format(
    cidade.lower().split()[0] in 'santo'))
