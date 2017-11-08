def converte_lst(lista):
    for c in lista:
        if c>9 or c<0:
            print('Apenas números de 0 a 9')
            break
    else:
        num10=''
        for i in lista:
            num10=num10+str(i)
        print(num10)
