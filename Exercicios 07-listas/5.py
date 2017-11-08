def soma_colunas(l):
    l1=[]
    for c in range(len(l)):
        x=0
        for i in range(len(l[c])):
            x=x + l[i][c]
        l1.append(x)
    print(l1)
