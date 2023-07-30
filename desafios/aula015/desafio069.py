cont = n = 0
while True:
    n = int(input('Informe um número: '))
    cont = 0
    if n > -1:
        while cont <= 10:
            print(f'{n}x{cont}={n*cont}')
            cont += 1
    else:
        break
print('Valor negativo não conta, programa encerrado!')