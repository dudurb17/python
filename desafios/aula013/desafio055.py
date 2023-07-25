
# frase = str(input('Informe a sua frase: ')).lower().strip()
# frase = frase.split()
# fraseC = frase
# frase = ''.join(frase)
# fraseC.reverse()
# fraseC = ''.join(fraseC)
# print(frase)
# print(fraseC)
# if frase == fraseC:
#     print('A frase é palindromo')
# else:
#     print('A frase não é palindromo')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
# for letra in range(len(junto)-1, -1, -1):
#     inverso += junto[letra]

if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
