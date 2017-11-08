adeptos = {'benfica': ['joao', 'ana', 'carla'], 'sporting': ['hugo', 'patricia'], 'porto': ['jose']}


def consulta_clube(nome, d):
    for i in d.keys():
        if nome in d[i]:
            return i
    return None


def mais_adeptos(d):
    n_adeptos = {}
    for i in d.keys():
        n_adeptos[i] = len(d[i])
        maximo = n_adeptos[i]
    max_lista = []
    for i in d.keys():
        if n_adeptos[i] >= maximo:
            maximo = n_adeptos[i]
        if n_adeptos[i] < maximo:
            del n_adeptos[i]
    for i in n_adeptos.keys():
        max_lista.append(i)
    s = '{0}'.format(max_lista[0])
    for i in range(1, len(max_lista)):
        s += ' e {0}'.format(max_lista[i])
    return s