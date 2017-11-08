n=int(input('Qual o numero? '))
n1=n
c=n
if n==0:
    print('O fatorial de ', n1, ' é ',1)
else:
    while n<0:
        print('Valor negativo')
        n=int(input('Qual o numero? '))
        c=n
        n1=n
    while n>1:
        c=c*(n-1)
        n=n-1
    print('O fatorial de ', n1, ' é ',c)

    


