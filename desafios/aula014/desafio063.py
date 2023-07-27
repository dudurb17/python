num = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razao da PA: '))
c = 10
print('Os dez priemiros termos são:')
while c > 0:
    print('{}'.format(num), end="->")
    num += razao
    c -= 1
print('FIM')
