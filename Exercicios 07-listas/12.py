nomes=[]

mensagem='\nIndique a sua opção:\
\nAdicionar nome (1), consultar lista (2), retirar os primeiros n (3), sair (0)'

while True:
    print(mensagem)
    op=int(input('Opção -> '))
    if op==0:
        break
    if op==1:
        nomes.append(str(input('Nome a adicionar -> ')))
    if op==2:
        print('Comprimento da fila: ', len(nomes))
        for i in nomes:
            print('- ', i)
    if op==3:
        retirar=int(input('Quantos nomes conseguem vaga e saem da fila? -> '))
        for i in range(retirar):
            nomes.pop(0)
print('----Fim de execução----')
    
      
    
