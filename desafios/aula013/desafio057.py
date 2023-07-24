maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Informe o seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
    if c == 0:
        menor = peso
print('O maior peso foi {} e o menor peso foi {}'.format(maior, menor))
