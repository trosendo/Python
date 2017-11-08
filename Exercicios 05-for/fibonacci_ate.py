def fibonacci_ate(v):
    l=[]
    l.append(1)
    l.append(1)
    i=1
    s=0

    while s<=v:
        s=l[i]+l[i-1]
        if s>v:
            break
        l.append(s)    
        i+=1

    return l

        

