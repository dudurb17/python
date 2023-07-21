import datetime
hoje = datetime.date.today()
ano = int(input('Informe o ano do seu nascimento: '))

idade = hoje.year-ano

if idade <= 9:
    print('Você é mirim')
elif idade > 9 and idade <= 14:
    print('Você é Infantil')
elif idade > 14 and idade <= 19:
    print('Você é junior')
elif idade > 19 and idade <= 20:
    print('Você é sênior')
else:
    print('Você é master')
