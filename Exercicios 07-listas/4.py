def conta_elementos(l, l1):
    c=0
    for i in range(len(l)):
        if l[i] in l1:
            c+=1
    print(c)
