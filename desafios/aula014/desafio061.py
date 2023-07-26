
finalizar="N"
opcao=4
while finalizar=="N":
    if opcao==4:
        num1=int(input("Informe o primeiro número: "))
        num2=int(input("Informe o segundo número: "))
    opcao=int(input(''' Informe o que você deseja fazer com o numero
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] sair do Programa
    Sua opção:''' ))
    if opcao==1:
        print("A soma do numero {} e do número {} é de {}".format(num1,num2, num1+num2))
    elif opcao==2:
        print("A multiplicação do numero {} e do número {} é de {}".format(num1, num2, num1*num2))
    elif opcao==3:
        if num1>num2:
            print("O maior número é o {}".format(num1))
        else:
             print("O maior número é o {}".format(num2))
    elif opcao==5:
        finalizar="S"
    else:
        print("Opção invalida")