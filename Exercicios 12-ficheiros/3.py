def processa_notas(nome):
    string=''
    dicionario={}
    for i in nome:
        if i!='\n':
            string=i.strip()
            lista=string.split(';')
        dicionario[lista[0]]=int(lista[1]), int(lista[2])
    return dicionario



f=input('Insira o nome do ficheiro (notas.txt): ')

nome=open(f, 'r')

print(processa_notas(nome))

nome.close()















