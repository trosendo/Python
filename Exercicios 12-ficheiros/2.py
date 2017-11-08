def conta_alunos(nome):
    x=0
    for i in nome:
        if i=='\n' or i=='':
            continue
        x+=1
    return x

f=input('Insira o nome do ficheiro (notas.txt): ')

nome=open(f, 'r')

print('O número de alunos é {0}'.format(conta_alunos(nome)))

nome.close()

