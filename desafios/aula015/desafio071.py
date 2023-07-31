maiores = homens = mulheres = 0
while True:
    idade = int(input('Informe a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo: [M/F] ')).upper().split()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulheres += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(
            input('Informe se deseja continuar: [S/N]')).upper().split()[0]
    if opcao == 'N':
        break
print(f'A quantidade de pessoas com mais de 18 anos é {maiores}!')
print(f'A quantidade de homens cadastrados foi de {homens}!')
print(f'A quantidade de mulheres com menos de 20 anos é de {mulheres}!')
