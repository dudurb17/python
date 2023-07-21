casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o seu salario: '))
ano = int(input('Informe em quantos anos quer pagar: '))

prestacao = casa/(ano*12)
if (salario*0.3) >= prestacao:
    print('O emprestimo foi aprovado')
else:
    print('O emprestimo foi negado!!')
