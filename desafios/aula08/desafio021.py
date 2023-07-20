import random
aluno1 = input('Informe o primeiro aluno: ')
aluno2 = input('Informe o segundo aluno: ')
aluno3 = input('Informe o terceiro nome: ')
aluno4 = input('Informe o quarto nome: ')
lista = [aluno1, aluno2, aluno3, aluno4]

print('O aluno sorteado para apagar o quadro foi o {}'.format(random.choice(lista)))
