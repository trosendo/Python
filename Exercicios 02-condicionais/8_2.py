def distancia(vel):
    d=1/2*(vel/10)**2
    return d

v=int(input('Qual a velocidade do carro em km/h? '))

print('A distância de travagem do carro a ', v, 'km/h é ', distancia(v), 'm') 
