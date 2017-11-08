def max_lista(lista):
    c=0
    maximo=0
    if len(lista)==0:
        print(maximo)
    else:
        while lista[c]>maximo:
            maximo=lista[c]
            c=c+1
        print(maximo)
    
