
frase = str(input('Informe a sua frase: ')).strip()
frase = frase.split()
fraseC = frase
frase = ''.join(frase)
fraseC.reverse()
fraseC = ''.join(fraseC)
print(frase)
print(fraseC)
if frase == fraseC:
    print('A frase é palindromo')
else:
    print('A frase não é palindromo')
