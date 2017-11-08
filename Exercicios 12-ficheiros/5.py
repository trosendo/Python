f=input('Insira o nome do ficheiro (notas.txt): ')

def conta_alunos(nome):
    x=0
    for i in nome:
        if i=='\n' or i=='':
            continue
        x+=1
    return x


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


def notas_ordem(dnotas):
    notas=[]
    notas2=[]
    for i in dnotas.values():
        notas.append((i[0], i[1]))
    notas.sort()
    for i in notas:
        notas2.append(i[1])
    return notas2
    

def escreve_notas(in_file, out_file):
    origem=open(in_file, 'r')
    destino=open(out_file, 'a')

    destino.write('# Prova de {:0>3} alunos'.format(conta_alunos(origem)))
    
    origem.close()
    origem=open(in_file, 'r')
    destino.write('\n# nota mais alta: {0[0]}, {0[1]}\n'.format(alunos_maior_nota(processa_notas(origem))))
    
    origem.close()
    origem=open(in_file, 'r')
    numeros_alunos=[]
    for i in processa_notas(origem).values():
        numeros_alunos.append(i[0])
    numeros_alunos.sort()

    origem.close()
    origem=open(in_file, 'r')
    
    for i in notas_ordem(processa_notas(origem)):
        x=0
        for c in numeros_alunos:
            if x==0:
                destino.write('{:0>5} = {:0>2}\n'.format(c, i))
                numeros_alunos.pop(0)
            x+=1
        origem.close()
        origem=open(in_file, 'r')
        
    origem.close()
    destino.close()

    
    
out_file=input('Insira o nome do ficheiro de destino a criar: ')

escreve_notas(f, out_file)
    

    
