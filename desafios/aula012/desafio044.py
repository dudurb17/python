lado1 = float(input('Informe a medida de um lado: '))
lado2 = float(input('Informe a medida do segundo lado: '))
lado3 = float(input('Informe a medida do terceiro lado: '))

if (lado1+lado2) > lado3 and (lado1+lado3) > lado2 and (lado2+lado3) > lado1:
    print('Pode se formar um triangulo')
    if lado1 == lado2 == lado3:
        print('O triangulo é equilatero')
    elif lado1 == lado2 != lado3 or lado3 == lado1 != lado2 or lado2 == lado3 != lado1:
        print('O triangulo é isosceles')
    else:
        print('O triangulo é Escaleno!')
else:
    print('Não é possivel se formar um triangulo!!')
