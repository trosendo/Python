def Sucessor(n):
    y=(n+1)
    return y;

def QuadradoDoSucessor(n):
    y=Sucessor(n)**2
    return y;

n=int(input('Insira un número inteiro: '))
print(QuadradoDoSucessor(n))
