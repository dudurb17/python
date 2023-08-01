lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# Tupla sao imutaveis
print(lanche[1])
print(lanche[1:3])
print(lanche[:2])
print(lanche[-3:])


for c in lanche:
    print(f'{c}', end=' ')
print('FIM DO FOR')

for cont in range(0, len(lanche)):
    print(cont)
    print(lanche[cont])
print('FIM DO FOR')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')


print(sorted(lanche))

a = (2, 5, 4)
b = (5, 6, 1, 2)
c = a+b
print(c)
print(c.count(5))
print(c.index(2))
del (c)
