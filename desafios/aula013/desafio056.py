import datetime
anoHj = datetime.date.today()
maiores = 0
for c in range(0, 7):
    ano = int(input('Informe o seu ano de nascimento: '))
    if (anoHj.year-ano) >= 18:
        maiores += 1
print('A quantidade de pessoas que ja cheagaram a mairidade foi de {} e as que não chegaram {}'.format(
    maiores, 7-maiores))
