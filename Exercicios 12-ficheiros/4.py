def processa_notas(nome):
    string=''
    dnotas={}
    for i in nome:
        if i!='\n':
            string=i.strip()
            lista=string.split(';')
        dnotas[lista[0]]=int(lista[1]), int(lista[2])
    return dnotas

def alunos_maior_nota(dnotas):
    x=0
    for i in dnotas.values():
        if x==0:
            maximo=i[1]
        if i[1]>maximo:
            maximo=i[1]
        x+=1
    nota_alunos=(maximo, [])
    for i in dnotas.keys():
        if dnotas[i][1]==maximo:
            nota_alunos[1].append(i)
    return nota_alunos



f=input('Insira o nome do ficheiro (notas.txt): ')

nome=open(f, 'r')

print(alunos_maior_nota(processa_notas(nome)))

nome.close()
