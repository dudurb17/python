reta1 = int(input('Informe a medida da priemira reta: '))
reta2 = int(input('Informe a medida da segunda reta: '))
reta3 = int(input('Informe a medida da terceira reta: '))

if (reta1+reta2) > reta3 and (reta1+reta3) > reta2 and (reta2+reta3) > reta1:
    print('Pode se formar um triangulo')
else:
    print('Não pode se formar um triângulo')
print('===FIM===')
