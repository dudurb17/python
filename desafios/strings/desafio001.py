frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])


print("""I stand among the brush staring at the sky, listening to mirror-clear water dribble down from a desert spring, looking at the mountain, strips of sandstone and red rocks powdered with trees and dust.""")


print(frase.count('o'))
print(frase.upper().count('O'))


frase = '    Curso em Vídeo Python     '
print(frase)
print(len(frase))
print(len(frase.strip()))


frase = 'Curso em Vídeo Python'
print(frase)
print(frase.replace('Python', 'Android'))
print(frase)
frase = frase.replace('Python', 'Android')
print(frase)
print('Curso' in frase)
print(frase.find('video'))
print(frase.lower().find('vídeo'))


print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2])
print(dividido[2][3])
