carrinho=[]

tabela=[['jarro',20.6],['almofada',18],['candeeiro',45]]
tabela.sort()

def adicionar(P,N):
    encontrado=False
    if len(carrinho)==0:
        carrinho.append([P,N])
    else:
        for i in carrinho:
            if P == i[0]:
                i[1]+=N
                encontrado=True
                break
        if encontrado==False:
            carrinho.append([P,N])
    return carrinho

def remover(P):
    c=0
    for i in carrinho:
        if P in i:
            carrinho.pop(c)
        c+=1
    return carrinho

def a_pagar():
    carrinho.sort()
    total=0
    for i in carrinho:
        for c in tabela:
            if i[0] == c[0]:
                total+=i[1]*c[1]
    print('Total= ', total, '€')

mensagem='\nIndique a sua opção:\
\n - Adicionar produtos ao carrinho (1) \n - Remover todas as unidades dum produto (2) \
\n - Mostrar o valor a pagar (3) \n - Sair (0)'

produtos=' - Jarro: 20.6/uni (1)\n - Almofada: 18/uni (2)\n - Candeeiro: 45/uni (3)'

while True:
    print(mensagem)
    op=int(input('Opção -> '))
    if op==0:
        break
    if op==1:
        print(produtos)
        op1=int(input('Produto a adicionar -> '))
        N=int(input('Quantidade -> '))
        if op1==1:
            P='jarro'
            adicionar(P, N)
        if op1==2:
            P='almofada'
            adicionar(P, N)
        if op1==3:
            P='candeeiro'
            adicionar(P, N)
    if op==2:
        print(produtos)
        op1=int(input('Produto a remover -> '))
        if op1==1:
            P='jarro'
            remover(P)
        if op1==2:
            P='almofada'
            remover(P)
        if op1==3:
            P='candeeiro'
            remover(P)
    if op==3:
        a_pagar()
print('----Fim de execução----')
        


        
