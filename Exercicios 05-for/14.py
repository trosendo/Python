import itertools

def fibonacci_ate(v):
    c=0
    l=[None]
    for i in itertools.count():
        if i<1:
            l[i]=1
            l=l+[None]
            l[i+1]=1
            if v==1:
                break
        elif i>=2 and v>1:
            c=l[i-2]+l[i-1]
            if c>v:
                break
            if l[i-1]+l[i-2]<=v:
                l=l+[None]
            l[i]=c
    print(l)











 
