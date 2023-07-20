salario = float(input('Informe o seu sálario: R$ '))
if salario > 1250:
    print('O seu salário é de R$ {:.2f} e com aumento de 10% vai ficar R$ {:.2f}'.format(
        salario, salario*1.10))
else:
    print('O seu salário era de R$ {:.2f} e com aumento de 15% vai ficar R$ {:.2f}'.format(
        salario, salario*1.15))
print('===FIM==')
