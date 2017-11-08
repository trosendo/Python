def matriz_identidade(l):
    indice=[]
    matriz=False
    for i in range(len(l)):
        if l[i].count(1)==1 and l[i].count(0)==len(l[i])-1:
            indice.append(l[i].index(1))
    if len(indice)!=len(l):
        return False
    for c in range(len(indice)):
        if indice[c]==c:
            matriz=True
    return matriz
        
        
        
        
