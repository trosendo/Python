def posição(p0, v0, t, a):
    p=p0+v0*t+1/2*a*t**2
    return p;

p0=float(input('Posição inicial: '))
v0=float(input('Velocidade incial: '))
t=float(input('Segundos após ter saído da posição incial: '))
a=float(input('Aceleração: '))

print(posição(p0, v0, t, a), ' é a posição do carro ', t, ' segundos após ter saído da posição inicial (', p0, ')')
