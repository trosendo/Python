def matriz(x, y):
    matriz=[]
    for i in range(x):
        linha=[]
        for j in range(y):
            s='{0}x{1}'.format(i+1, j+1)
            linha.append(s)
        matriz.append(linha)
    for i in matriz:
        print(i)

    return matriz
