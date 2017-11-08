def velocidade(v0, a, t):
    v=v0+a*t
    return v;

v0=float(input('Insira o valor da velocidade inicial (m/s): '))
a=float(input('Insira o valor da aceleraão do carro (m/s^2): '))
t=float(input('Indique o tempo decorrido desde a recolha da velocidade inicial (s): '))

print('A velocidade do carro ', t, ' segundos após a recolha da velocidade inicial é ', velocidade(v0, a, t), ' m/s')
