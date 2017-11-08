a=int(input('1º Número: '))
b=int(input('2º Número: '))
c=int(input('3º Número: '))

if min(a, b, c) < a < max(a, b, c):
    meio=a
elif min(a, b, c) < b < max(a, b, c):
    meio=b
else:
    meio=c
    
print('O valor do meio é ', meio)

