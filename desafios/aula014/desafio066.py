n = 0
quantas = 0
soma = 0
while n != 999:
    n = int(input('Informe o valor: '))
    if n != 999:
        quantas += 1
        soma += n
print('A quantidade de números digitados foi de {} e a soma deles é {}'.format(
    quantas, soma))
