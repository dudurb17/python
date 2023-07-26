import random
pc=random.randrange(0,10)
print(pc)
tentativas=0
terminou="N"
while terminou=="N":
    user=int(input("Informe o valor de 0 a 10: "))
    if user==pc:
        terminou="S"
    tentativas+=1
print("Parabens você acertou o número que o pc pensou em {} tentativas".format(tentativas))