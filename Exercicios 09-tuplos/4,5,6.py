pos=[('joao',300,20),('ana',80,15),('patricia',17,90)]

#4

def coordenadas(pos,nome):
    for i in range(len(pos)):
        for c in pos[i]:
            if c==nome:
                coordenadas=pos[i][1], pos[i][2]
                return coordenadas


#5

def acima(pos,y):
    nomes=[]
    for i in pos:
        if i[-1]>y:
            nomes.append(i[0])
    return nomes


#6

def direita(pos, x):
    nomes=[]
    for i in pos:
        if i[1]>x:
            nomes.append(i[0])
    return nomes
