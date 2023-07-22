import random
pc = random.randrange(1, 4)

usuario = int(
    input('Informe o que você vai jogar:\n1-papel\n2-tesoura\n3-pedra:\n'))

if pc == 1 and usuario == 3 or pc == 2 and usuario == 1 or pc == 3 and usuario == 2:
    print('Você perdeu!!')
elif usuario == 1 and pc == 3 or usuario == 2 and pc == 1 or usuario == 3 and pc == 2:
    print('Você ganhou!!')
else:
    print('Deu empate')
