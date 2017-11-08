num=int(input('Insira um número com 3 algarismos: '))

centenas=num//100
unidades=num%10

if centenas==unidades:
    print('O número ', num, ' é uma capicua')
else:
    print('O número ', num, ' não é uma capicua')
