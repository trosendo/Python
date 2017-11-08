import math

def distancia(x1, y1, x2, y2):
    'Distância entre dois pontos'
    d=round(math.sqrt((x2-x1)**2+(y2-y1)**2), 2)
    return d;

print('Introduza as coordenadas do ponto 1')
x1=float(input('X1: '))
y1=float(input('Y1: '))

print('Introduza as coordenadas do ponto 2')
x2=float(input('X2: '))
y2=float(input('Y2: '))

print(distancia(x1, y1, x2, y2), ' é a distância entre os dois pontos.')
