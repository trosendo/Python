def multiplo(n,m):
    multiplo=False
    if n%m==0:
        multiplo=True
    return multiplo

num1=int(input('1º Número: '))
num2=int(input('2º Número: '))

if multiplo(num1, num2)==True:
    print(num1, ' é multiplo de ', num2)
else:
    print(num1, ' não é multiplo de ', num2)

    
