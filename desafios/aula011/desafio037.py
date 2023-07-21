print('\033[1;31;43mOlá mundo\033[m')
nome = 'Eduardo'
print('Olá! Muito preazer em te conhecer, {}{}{}!!!'.format(
    '\033[4;34m', nome, '\033[m'))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Ola! Muito prazer em te conhecer, {}{}{}!!!'.format(
    cores['pretoebranco'], nome, cores['limpa']))
