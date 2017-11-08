import re

num=int(input('Insira um numéro: '))

if len(str(num))>2:
    print('Apenas 2 algarismos permitidos!')
else:
    num_dividido_10=num/10

    split_num_dividido=str(num_dividido_10).split('.')

    num1=int(split_num_dividido[0])

    num2=int(split_num_dividido[1])

    print('\t', num1, '\n\t', num2)
    
