continuar = "S"
maior = menor = 0
cont = 0
soma = 0
while continuar == 'S':
    n = int(input('Informe o número: '))
    soma += n
    if cont == 0:
        maior = menor = n
    cont += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    continuar = str(
        input('Informe se deseja colocar outro número: [S/N]: ')).upper()
print('A media dos numeros é de {}.\nO maior número: {}\nO menor número: {}'.format(
    soma/cont, maior, menor))
