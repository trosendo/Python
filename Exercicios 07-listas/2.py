def verifica_ordem(l):
    l1=l[:]
    l.sort()
    if l==l1:
        return True
    else:
        return False
    
