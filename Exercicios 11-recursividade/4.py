def letras(str):
    lista=[]
    for i in str:
        if i in lista:
            continue
        lista.append(i)
    return lista


def in_lista(c, x):
    if c in x:
        return True
    return False


def letras_recursiva(str):
    separa=' '.join(str)
    lista=separa.split()
    
    if len(str)>1:
        if not in_lista(str[0:1], str[1:].split()):
            
    else:
        return [str]
    return letras_recursiva(str)+letras_recursiva(str[1:])
