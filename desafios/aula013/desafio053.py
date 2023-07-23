num = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo = num + (10-1)*razao
for c in range(num, decimo, razao):
    print(c)
