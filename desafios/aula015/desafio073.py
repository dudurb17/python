valor = int(input('Informe o valor a ser sacado: '))
cinquenta = vinte = dez = hum = 0
cinquenta = valor//50
valor -= cinquenta*50
vinte = valor//20
valor -= vinte*20
dez = valor//10
valor -= dez*10
hum = valor//1
print(cinquenta)
print(vinte)
print(dez)
print(hum)


# metodo diferente

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Informe o valor a ser sacado: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} células de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao Banco CEV! tenha um bom dia')
