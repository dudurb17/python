velocidade = int(input('Informe a sua velocidade: '))
if velocidade > 80:
    multa = (velocidade-80)*7
    print('Você foi multado por ultrapassar a velocidade permitida de 80 Km/h e tera que pagar a multa de R$ {}'.format(multa))
else:
    print('Tudo certo, nao foi multado')
print('===FIM===')
