import datetime

hoje = datetime.date.today()

dia = int(input('Informe o dia que nasceu: '))
mes = int(input('Informe o mês que nasceu: '))
ano = int(input('Informe o ano que nasceu: '))

data = datetime.date(ano, mes, dia)

idadeY = hoje.year-data.year
idadeM = hoje.month-data.month
idadeD = hoje.day - data.day

if idadeY < 18:
    print('Ainda falta para se alistar {} dias, {} meses e {} anos'.format(
        idadeD, idadeM, 18-idadeY))
elif idadeY == 18 and idadeM < 6 or idadeY == 18 and idadeM == 6 and idadeD < 0:
    print('Está na hora de se alistar')
else:
    print('Passou do temppo de se alistar, você está atrasado em {} dias, {} meses e {} anos'.format(
        idadeD*-1, idadeM, idadeY-18))
