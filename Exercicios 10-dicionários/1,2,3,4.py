ltel= {'joao':961111, 'ana':932222, 'carla':913333, 'manuel':964444}

def encontra_telefone(nome, ltel):
    if nome in ltel:
        return ltel[nome]
    return 0
        
    

def novo(nome, tel, dic):
    dic[nome]=tel
    

def cliente(tel, ltel):
    for c in ltel:
        if ltel[c]==tel:
            return c
    return 'DESCONHECIDO'


def mostra_lista(ltel):
    a=list(ltel.keys())
    a.sort()
    for c in a:
        print('{}: {}'.format(c, ltel[c]))
        
