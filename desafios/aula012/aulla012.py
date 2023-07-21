nome = str(input('Informe o seu nome: '))
if nome == 'Eduardo':
    print('Que nome bonito')
elif nome == 'Fernando':
    print('Nome do meu irmão')
elif nome in 'Ana Claudia Juliana':
    print('Nome feminino normal')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}'.format(nome))
