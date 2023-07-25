# num = int(input('Informe o número: '))
# mult = 0
# for c in range(2, num):
#     if num % c == 0:
#         mult += 1
# if mult == 0:
#     print('O número é primo')
# else:
#     print('O numero nao é primo!!')
num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')

print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('O numero é primo')
else:
    print('Não é primo')
