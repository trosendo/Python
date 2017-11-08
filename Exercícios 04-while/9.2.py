a=int(input('valor a: '))
b=int(input('valor b: '))

c=1

while c<=50:
    a1=c%a
    b1=c%b
    if a1==0 or b1==0:
       print(c)
        
    c+=1
