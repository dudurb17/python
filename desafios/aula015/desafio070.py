import random
acerto=0
while True:
    pc = random.randrange(0, 11)
    opcao = str(input('Par ou ímpar? [P/I]')).upper().split()
    n = int(input('Informe um número: '))
   
    if (pc+n) % 2 == 0:
        jogo = 'PAR'
    else:
        jogo = 'IMPAR'
    print(f'Você jogou {n} e o computador {pc}. Total de {pc+n} e DEU {jogo}')
    if opcao == 'I' and jogo == 'IMPAR' or opcao == 'P' or jogo == 'PAR':
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        acerto+=1
    else:
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {acerto} vezes.')
