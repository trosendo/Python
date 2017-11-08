M=['tomás', 'miguel', 'marco']
N=['tomás tomás miguel', 'miguel miguel tomás', 'marco marco miguel']
MxN=[]
MxN.append(M)
MxN.append(N)
print(MxN)
def mostraMatriz(tabela):
        M=[]
        for pal in MxN:
                for doc in MxN:
                        x=0
                        if pal in doc:
                                for item in doc:
                                        if item==pal:
                                                x+=1
                        else:
                                continue
                M.append([pal, doc, x])
        print(M)





















def main(M,N):
    #M - palavras chave // N - Documentos
    matriz=[]
    a=0
    x=0
    
    for i in range(len(N)):
        matriz.append([N[i], None])
    print(matriz)

    for i in matriz:
        for c in M:
            n=N[a].split()
            for v in n:
                print(v)
                if v==M[a]:
                    x+=1
        matriz[a][1]=x
        a+=1
    print(matriz)
            
            

























    
def outra():
    n=N.split()
    m=M.split()
    matriz=[]
    
    for i in n:
        for c in m:
            if c==i:
                x=0
                x+=1
                if len(matriz)==0:
                    matriz.append([c,x])
                for x in matriz:
                    if c != x[0]:
                        matriz.append([c,x])
                x=0
            
    print(matriz)
