def bissexto(ano):
    'Verificação de ano bissexto'
    return (ano%400==0 or (ano%4==0 and ano%100!=0));

ano=int(input('Introduza um ano: '))

if bissexto(ano)==True:
    print('O ano ', ano, ' é bissexto.')
else:
    print('O ano ', ano, ' não é bissexto.')


