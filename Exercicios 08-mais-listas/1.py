def count(E, L):
    c=0
    if type(L)==str:
        L=L.split()
    for i in L:
        if i==E:
            c+=1
    return c


def In(E, L):
    for i in L:
        if i==E:
            return True
    return False

def reverse(L):
    L=L[::-1]
    return L

def index(E, L):
    i=0
    for c in L:
        if c==E:
           return i
        i+=1

def insert(I, E, L):
    i=0
    L_insert=[E]
    for c in range(len(L)):
        if c == I:
            break
        i+=1
    L_1=L[0:i]
    L_2=L[i:len(L)]
    L_new=L_1+L_insert+L_2
    return L_new

def append(L1, L2):
    L=L1+L2
    return L


def remove(E, L):
    i=index(E, L)
    L1=L[:i]
    L2=L[i+1:]
    L_new=L1+L2
    return L_new


def pop(I, L):
    L_new=remove(L[I], L)
    return L_new

