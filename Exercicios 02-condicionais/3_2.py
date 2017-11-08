import math

num=int(input('Qual o número: '))

if num>=0:
    raiz=math.sqrt(num)
    print('A raiz quadrada de ', num, ' é ', raiz, '.')
else:
    print('O número inserido foi negativo.')
