import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('Raiz arredondada para cima {} '.format(math.ceil(raiz)))
print('Raiz arredondada para baixo {} '.format(math.floor(raiz)))

