num1 = int(input('Informe o valor para mostrar a tabuada: '))
print('Tabuada do valor {}!'.format(num1))
for i in range(0, 11):
    print('{}x{}={}'.format(num1, i, num1*i))
