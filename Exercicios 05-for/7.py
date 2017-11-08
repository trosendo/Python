def e_primo(n):
    primo=True
    if n==4 or n==0 or n==1:
        primo=False
    for i in range(3, n):
        if n%i==0:
            primo=False
#    if primo:
#        print('O número', n, 'é primo')
    return primo
        
def mostra_primos():
    n=int(input('Introduza um valor: '))
    for i in range(2, n+1):
        if e_primo(i):
            print('O número', i, 'é primo')
    
mostra_primos()
