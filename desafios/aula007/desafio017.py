dia=int(input('Informe quantos dias voc~e utilizou o carro: '))
km=int(input('Informe quantos Km rodados'))
valor=(dia*60)+(km*0.15)
print('O valor sera pago por andar {} dias e andar {} km será de {} '.format(dia,km, valor))