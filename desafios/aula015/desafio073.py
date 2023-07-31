valor = int(input('Informe o valor a ser sacado: '))
cinquenta = vinte = dez = hum = 0
cinquenta = valor//50
valor -= cinquenta*50
vinte = valor//20
valor -= vinte*20
dez = valor//10
valor -= dez*10
hum=valor//1
print(cinquenta)
print(vinte)
print(dez)
print(hum)