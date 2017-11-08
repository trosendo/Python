print('Insira as coordenadas x e y:')
x=float(input('X: '))
y=float(input('Y: '))

if (x>0 and y>0):
    true='1º Quadrante' 
if (x<0 and y>0):
    true='2º Quadrante' 
if (x<0 and y<0):
    true='3º Quadrante' 
if (x>0 and y<0):
    true='4º Quadrante' 

print('O ponto de coordenadas (', x, ',', y, ') pertence ao ', true)
