distancia = int(input('Informe a distancia da viagem: '))
if distancia < 200:
    print('O valor a ser pago será de R$ {}'.format(distancia*0.50))
else:
    print('O valor a ser pago será de R$ {}'.format(distancia*0.45))
print('===FIM===')
