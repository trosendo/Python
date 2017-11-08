#5.
def conta_palavras(x):
    count=0
    p=0
    lista=list(x) 
    while p<len(lista):
        if lista[p]==',':
            if lista[p-1]!=',' and lista[p-1]!='.' and lista[p-1]!=' ': 
                count+=1
        if lista[p]==' ':
            if lista[p-1]!=',' and lista[p-1]!='.' and lista[p-1]!=' ': 
                count+=1
        p+=1
    if p==len(lista):
        if lista[p-1]!=',' and lista[p-1]!='.' and lista[p-1]!=' ': 
            count+=1
    return count

#1.1
def letras(x):
    lista=list(x)
    z=lista[::-1]
    for i in z:
        print(i)

#1.2
def escala_in(x):
    z=len(x)
    while z>0:
        y=x[:z]
        print(y)
        z-=1

#2.
def find(x,y,z):
    while z<len(x):
        if x[z]==y:
            return z
        z+=1
    return('A palavra inserida não contém o caracter indicado')

#3.
#Exemplos:
def troca(x):
    print(x.replace('a','A'))


def apaga(x):
    print(x.strip('w.compt'))

#4.
def espelho_simples(x):
    return x+x[::-1]


def espelho_sem_truques(x):
    r=[]
    count=-1
    while count>=-len(x):
        r.append(x[count])
        count+=-1
    y=''.join(r)
    return x+y

#6.
def le_palavras(x):
    n=0
    fin=open('words.txt')
    print(fin)
    lista=list(fin)
    while n<len(lista)-1:
        if len(lista[n])==x:
            print(lista[n])
            n+=1

fin=open('forca_palavras.txt')
print(fin)
    



