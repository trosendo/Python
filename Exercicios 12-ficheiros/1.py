origem=str(input('Insira o nome do ficheiro de origem: '))
destino=str(input('Insira o nome do ficheiro de destino: '))

f_origem=open(origem, 'r')
f_destino=open(destino, 'r+')

s=f_origem.read()
f_destino.write(s)
f_destino.flush()

f_origem.close()
f_destino.close()

f_destino=open(destino, 'r+')
s2=f_destino.read()

if s==s2:
    print('Cópia bem sucedida!')
else:
    print('Cópia mal sucedida!')

f_origem.close()
f_destino.close()
