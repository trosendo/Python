def fibonacci(n):
    l=[None]*(n)
    for i in range(0, n):
        if i<2:
            l[i]=1
        else:
            l[i]=l[i-2]+l[i-1]
    print(l)
