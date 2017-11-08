a=int(input('valor a: '))
b=int(input('valor b: '))

c=1

while c<=50:
    a1=c%a
    b1=c%b
    if a1==0 and b1==0:
        print(c, ' é multiplo de ', a, ' e de ', b)
    elif a1==0:
        print(c, ' é multiplo de ', a)
    elif b1==0:
        print(c, ' é multiplo de ', b)
        
    c+=1
