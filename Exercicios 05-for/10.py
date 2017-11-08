def media_acima(lista, valor):
    c=0
    l=0
    for i in lista:
        if i>=valor:
            c=c+i
            l=l+1
    media=c/l
    print('A média dos valores da lista acima de', valor, 'é', media)



