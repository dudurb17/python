import math

catetoOp = float(input('Informe o comprimento do cateto oposto: '))
catetoAdj = float(input('Informe o comprimento do cateto adjacente: '))
print('O cateto oposto é {}, cateto adjacente {} e a hipotenusa {:.2f}'.format(
    catetoOp, catetoAdj, math.hypot(catetoOp, catetoAdj)))
