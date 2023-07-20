frase = str(input('informe uma frase: '))

print('A frase é {}'.format(frase))
print('Nessa frase tem {} letras a'.format(frase.lower().count('a')))
print('O primeiro a esta na posiçao {}.'.format(frase.lower().find('a')))
print('O ultimo a está na posição {}.'.format(frase.lower().rfind('a')))
