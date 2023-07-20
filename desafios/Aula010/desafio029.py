import random
valor = random.randrange(0, 6)
num = int(input('Informe um valor de 0 a 5: '))

if valor == num:
    print('Parabéns, você acertou o número!!')
else:
    print('Infelizmente, nao foi dessa vez')
print('===FIM===')
