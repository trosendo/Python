def meio(lista):
    lista1=lista[:]
    lista1.pop(0)
    lista1.pop(len(lista1)-1)
    print('Lista=', lista, '\nLista 1=', lista1)
