def e_primo(n):
    primo=True
    if n==4 or n==0 or n==1:
        primo=False
    for i in range(3, n):
        if n%i==0:
            primo=False
    if primo:
        print('O número', n, 'é primo')
