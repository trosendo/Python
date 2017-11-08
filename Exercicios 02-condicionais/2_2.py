import math

def p(r):
    'Perimetro circunferencia'
    p=2*math.pi*r
    return p;

def a(r):
    'Área do circulo'
    a=math.pi*r**2
    return a;

def v(r):
    'Volume da esfera'
    v=(4/3)*math.pi*r**3
    return v;

r=float(input('Qual o raio? '))

print('Perímetro da circunferência = ', p(r), '\nÁrea do círculo = ', a(r), '\nVolume da esfera = ', v(r))
