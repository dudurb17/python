valor = float(input('Informe o valor da compra: '))
opcao = int(input('Informe a forma de pagamento:\n1-dinheiro/cheque\n2-cartão\n'))

if opcao == 1:
    print('Você ganhou 10% de desconto e pagará R$ {}'.format(valor*0.9))

elif opcao == 2:
    vezes = int(input('Informe quantas vezes você quer fazer: '))
    if vezes == 1:
        print('Você ganhou 5% de desconto e pagará R$ {}!!'.format(valor*0.95))
    elif vezes == 2:
        print('Você não ganhou desconto e pagará o valor cheio de R$ {}'.format(valor))
    elif vezes >= 3:
        print('Você pagará 20% a mais e pagará R$ {}'.format(valor*1.2))
    else:
        print('Quantidade de parcela indisponivel')
