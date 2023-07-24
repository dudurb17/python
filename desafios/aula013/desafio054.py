num = int(input('Informe o número: '))
mult = 0
for c in range(2, num):
    if num % c == 0:
        mult += 1
if mult == 0:
    print('O número é primo')
else:
    print('O numero nao é primo!!')
