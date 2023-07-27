num = int(input('Informe o número: '))
c = num
valorT = 1
print('Calculando {}!='.format(num), end=' ')
while c > 0:
    print("{}".format(c), end='')
    print(" x " if c > 1 else ' = ', end='')
    valorT *= c
    c -= 1
print(valorT)

c = 0
valorT = 1
for c in range(num, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    valorT *= c

print(valorT)
