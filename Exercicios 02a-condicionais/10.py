def triangulo(a, b, c):
    triangulo=False
    if a+b>c and a+c>b and b+c>a:
        triangulo=True
    else:
        return print('Não existe triângulo com estes valores');

    if a==b==c:
        print('O triângulo é equilátero')
    elif a==b or a==c or b==c:
        print('O triângulo é isósceles')
    else:
        print('O triângulo é escaleno')
    return;




