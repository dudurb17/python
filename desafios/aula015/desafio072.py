barato = maisMil = total = 0
nomeBarato = ''
while True:
    nome = str(input('Informe o nome do produto: ')).strip()
    valor = float(input('Informe o valor do produto: R$ '))
    if nomeBarato == '':
        barato = valor
        nomeBarato = nome
    total += valor
    if valor >= 1000:
        maisMil += 1
    if valor < barato:
        barato = valor
        nomeBarato = nome
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(
            input('Informe se deseja continuar: [S/N]')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'O valor da compra é {total:.2f}!')
print(f'A quantidade de produto que custa mais de mil foi de {maisMil}!')
print(f'O produto mais barato é o {nomeBarato} que custou {barato:.2f}')
