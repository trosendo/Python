def bin_div(list, number):
    bin_to_decimal=[]
    divisiveis=[]
    dec=[]
    divisivel=0
    x=0
    for i in list:
        bin_to_decimal.append(int(str(i), 2))
    
    for i in bin_to_decimal:
        if i%number==0:
            if i!=0:
                divisivel=int(bin(i)[2:])
                divisiveis.append(divisivel)
                dec.append(i)
        x+=1
    print('Decimais=', dec)
    return divisiveis
    
