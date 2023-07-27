n = int(input('Informe um número: '))
a = 0
b = 1
c = 0
while c < n:
    print(a, end='->')
    auxiliar = a+b
    a = b
    b = auxiliar
    c += 1
print('Fimm')
