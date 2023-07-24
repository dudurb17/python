maisV = ''
idadeV = 0
mulheres = 0
mediaIdade = 0
for c in range(0, 4):
    nome = str(input('Informe seu nome: '))
    idade = int(input('Informe sua idade: '))
    mediaIdade += idade
    sexo = int(input('Informe seu sexo:\n1-Masculino\n2-Feminino\nSua opção: '))
    if idade > idadeV and sexo == 1:
        maisV = nome
        idadeV = idade
    if idade < 20 and sexo == 2:
        mulheres += 1
print('A media da idade do grupo é {}'.format(mediaIdade/4))
print('O homem mais velho é o {} com a idade de {}'.format(maisV, idadeV))
print('A quantidade de mulheres com menos de 20 anos é de {}'.format(mulheres))
