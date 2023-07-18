import math
angulo = int(input('Informe o angulo'))
cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O angulo {} informado foi O cosseno é {:.2f} O seno é {:.2f}A tangente é {:.2f}'.format(
    angulo, cosseno, seno, tang))
