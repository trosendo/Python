import math

num=float(input('Insira um número: '))
num_3_casas=round(num, 3)
split_num=str(num).split('.')
num_inteiro=int(split_num[0])
num_decimal=int(split_num[1])

#num_inteiro=int(num)           
#num_decimal=num-num_inteiro        Devolve valor decimal errado

print('Número com 3 casas decimais: ', num_3_casas)
print('Parte inteira: ', num_inteiro)
print('Parte decimal: ', num_decimal)
