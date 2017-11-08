for n in range(2,101):
    divisores=False
    for x in range(1,n//2):
        if n%x==0:
            divisores=True
            break
    if not divisores:
        print(n, 'é primo!')
