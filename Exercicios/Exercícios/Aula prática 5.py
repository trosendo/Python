#1.
def compara(x,y):
    if x>y:
        return 1
    if x==y:
        return 0
    return -1

#2.
def hipotenusa(x,y):
    z=(x**2+y**2)**(1/2)
    return round(z,4)

#3.
def ack(m,n):
    if isinstance(m,int) and isinstance(n,int) and m>=0 and n>=0:  
        if m==0:
            return n+1
        if n==0:
            return ack(m-1,1)
        return ack(m-1,ack(m,n-1))
    return('ERROR')

#5.
def palíndromo(palavra):
    lista=list(palavra)
    if lista[::1]==lista[::-1]:
        return 'A palavra inserida é um palíndromo'
    return 'A palavra inserida não é um palíndromo'

#6.
def mdc(A,B):
    if not isinstance(A,int)and isinstance(B,int): 
        if B==0:
            return A
        R=A%B
        return mdc(B,R)
    return ('ERROR')

#7.
def print_n(s, n):
    while n>0:
        print(s)
        if n<=0:
            return
        n-=1

#8.





        
        
    
        

