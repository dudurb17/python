nome = str(input('Informe seu nome: '))
print('O seu primeiro nome é {}.'.format(nome.split()[0]))
print('O seu ultimo nome é {}.'.format(nome.rsplit()[-1]))
