a=int(input('valor a: '))
b=int(input('valor b: '))

c=1

while c<=50:
    if c%a==0 or c%b==0:
        print(c)
    c+=1
