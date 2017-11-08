def custos_envio(n, custo1, custoN):
    custo=(n-1)*custoN+custo1
    return custo;

n=int(input('Nº de livros: '))
custo1=float(input('Custo para a primeria cópia (€): '))
custoN=float(input('Custo unitário para as seguintes (€): '))

print('Custo: ', custos_envio(n, custo1, custoN), '€')
