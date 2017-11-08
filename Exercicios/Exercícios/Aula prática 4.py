 #1.
def numero_par(x):
    if x%2==0:
        return True
    return False
#2.
def um_algarismo(x):
    if x<10:
        return True
    return False

#3.
def portas_lógicas(x,y,z):
    if x=='and':
        if y==z==True:
            return True
        y==z==False or y!=z
        return False
    if x=='or':
        if y==True or z==True:
            return True

#4.
def numero_meio(x,y,z):
    M=max(x,y,z)
    m=min(x,y,z)
    if x==M and y==m or x==m and y==M:
        return z
    if z==M and y==m or z==m and y==M:
        return x
    if x==M and z==m or x==m and z==M:
        return y
#5.
def triangulo(x,y,z):
    if x+y>z and x+z>y and y+z>x:
        print('Os valores', x, y, z,'formam um triângulo')
        if x==y==z:
            return 'equilátero'
        if x==y or x==z or y==z:
            return 'isósceles'
        return 'escaleno'
    return 'Não é possível formar um triângulo com os valores inseridos.'

#6.
def ano_bissexto(x):
    if x%4==0 and x%100!=0:
        return True
    if x%400==0:
        return True
    return False

def data_válida(x,y,z):
    if x==29 and y==2:
        if ano_bissexto(z)==True:
            return ('Data válida')
        return ('Data inválida')
    return('Data válida')

#7.1
def factorial_recursiva(x):
    if isinstance(x,int):
        if x<=1:
            return 1
        return x*factorial_recursiva(x-1)

#7.2
def factorial_iterativa(x):
    resultado=1
    if x==0 or x==1:
        return 1
    while x>0:
        resultado*=x
        x-=1
    return resultado

#8.1
def fibonacci_recursiva(x):
    if x==0:
        return 0
    if x==1:
        return 1
    return fibonacci_recursiva(x-1)+fibonacci_recursiva(x-2)
    
teste=fibonacci_recursiva(4)
print(teste)



