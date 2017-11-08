nome=open('notas.txt', 'r')

string=''
dicionario={}
for i in nome:
    #print(i)
    if i!='\n':
        string=i.strip()
        lista=string.split(';')
        #print(lista)
    dicionario[lista[0]]=int(lista[1]), int(lista[2])
print(dicionario)
        














