num = int(input('Informe o número: '))
opcao = int(input(
    'Informe o tipo que vc quer converter:\n1-Binário\n2-octal\n3-hexadecimal\nSua opção:'))
if opcao == 1:
    print('O valor digitado é {} e em binario fica {}'.format(num, bin(num)))
elif opcao == 2:
    print('O valor digitado é {} e em octal fica {}'.format(num, oct(num)))
elif opcao == 3:
    print('O valor digitado é {} e em hexadecimal fica {}'.format(num, hex(num)))
else:
    print('Opção invalida')
