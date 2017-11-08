litros=int(input('Quantos litros: '))
combustivel=0
preço=0
quantia=litros*1.149
quantia95=litros*1.364
quantia98=litros*1.414
while combustivel!='gasoleo' and combustivel!='gasolina95' and combustivel!='gasolina98':
    combustivel=str(input('Qual o combustivel? (gasoleo, gasolina95, gasolina98) '))
if combustivel!='gasolina98':
    dia=int(input('Qual o dia do abastecimento? '))
    while dia>31 or dia<=0:
        dia=int(input('Qual o dia do abastecimento? '))
    if dia>0 or dia<15:
        if combustivel=='gasoleo':
            preço=round(quantia, 2)
        elif combustivel=='gasolina95':
            preço=round(quantia95, 2)
        print('O custo de ', litros, ' litros de ', combustivel, ' no dia ', dia, ' é de ', preço, '€')
    elif dia>=15 or dia<=31:
        if combustivel=='gasoleo':
            quantia-=0.023
            preço=round(quantia, 2)
        elif combustivel=='gasolina95':
            quantia95-=0.021
            preço=round(quantia95, 2)
        print('O custo de ', litros, ' litros de ', combustivel, ' no dia ', dia, ' é de ', preço, '€')
else:
    preço=round(quantia98, 2)
    print('O custo de ', litros, ' litros de ', combustivel, ' é de ', preço, '€')
