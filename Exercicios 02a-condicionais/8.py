def tempoDecorrido(d, v):
    v_ms=v/3.6
    t=d/v_ms
    return t;




d=float(input('Distância a percorrer (m): '))
v=float(input('Velocidade (km/h): '))

print('Irá demorar ', tempoDecorrido(d, v), ' segundos a percorrer ', d, ' m à velocidade de ', v, ' km/h')




