nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1+nota2)/2

if media < 5:
    print('Infelizmente você foi reprovado')
elif media >= 5 and media < 6:
    print('Ficou em recuperção')
else:
    print('Você foi aprovado')
