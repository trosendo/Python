produtos=input('Lista de produtos(Ex.: \'Pão\', \'Iogurte\'): ')
quantidades=input('Lista de quantidades: ')
preços_uni=input('Lista de preços unitários: ')

prod=list(eval(produtos))
q=list(eval(quantidades))
p=list(eval(preços_uni))

for i in range(0, len(prod)):
    preço=0
    print(prod[i],':', q[i]*p[i], 'eur')
    preço=preço+q[i]*p[i]
    
print('TOTAL: ', preço, 'eur')
