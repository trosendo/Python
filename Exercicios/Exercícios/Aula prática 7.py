#1.
def soma_c(x):
    l=[]
    soma=0
    count=0
    while count<len(x):
        soma=soma+x[count]
        l.append(soma)
        count+=1
    return l

print(soma_c([9,9,9]))

#2.
#versão com truque
def verifica_ordem(x):
    z=sorted(x)
    if x==z:
        return True
    return False

#versão sem truque
def verifica_ordem_v1(x):
    n=len(x)
    count=0
    while count<=n-2:
        if x[count]<=x[count+1]:
            count+=1
        else:
            return False
    return True

#3.1.
def corta(x):
    del x[0]
    del x[len(x)-1]

#3.2.
def meio(x):
    l2=[]
    posição=1
    while posição<len(x)-1:
        l2.append(x[posição])
        posição+=1
    return l2

#4.
def e_anagrama(x,y):
    lista1=list(x)
    lista2=list(y)
    count=0
    while count<len(lista1):
        if lista1[count] in lista2:
            count+=1
        else:
            return('As palavras inseridas não são anagramas.')
    return('As palavras inseridas são anagramas.')

#5.
def conta_elementos(x,y):
    count=0
    posição=0
    while posição<len(x):
        if x[posição] in y:
            count+=1
        posição+=1
    return count

#test=conta_elementos([1,2,3,4],[2,4])
#print(test)

#6.
def soma_colunas(x):
    lista=[]
    soma=0
    l=0
    for c in range(0,len(x[0])):
        for l in range(0, len(x)):
            soma+=x[l][c]
            if l == len(x)-1:
                lista.append(soma)
                soma = 0
    return lista
    
            
  

#test = soma_colunas([[1,3,3],[3,4,5],[6,7,8]])
#print(test)

        
#7.
def matriz_identidade(x):
    diagonal = []
    posições = []
    for l in range(0,len(x)):
        for c in range(0,len(x[0])):
            if l == c :
                diagonal.append(x[l][c])
            else:
                posições.append(x[l][c])
    if not max(diagonal) == 1:
        return False
    if max(posições) == 0:
        return True
    return False
    
  
#test=matriz_identidade([[1,0,0],[0,1,0],[0,0,1]])
#print(test)
