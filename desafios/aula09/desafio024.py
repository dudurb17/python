num1 = int(input('informe um valor: '))
u = num1//1 % 10
d = num1//10 % 10
c = num1 // 100 % 10
m = num1//1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
