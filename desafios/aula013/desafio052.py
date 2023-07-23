s = 0
for c in range(0, 6):
    n = int(input('Informe o numero: '))
    if n % 2 == 0:
        s += n
print('O valor ficou em {}'.format(s))
