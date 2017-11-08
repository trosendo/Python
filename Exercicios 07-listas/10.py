def acumulado(l):
    l_new=[]
    x=0
    for i in range(len(l)):
        x+=l[i]
        l_new.append(x)
    print(l_new)
