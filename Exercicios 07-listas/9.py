def top3(lista):
    lista.sort()
    top3=lista[:3]
    return top3

n=[]
atletas=int(input('Quantos tempos pretende inserir? '))
for i in range(atletas):
    s='Tempo atleta {0}: '.format(i+1)
    x=float(input(s))
    n.append(x)
print('O top3 de ', n , 'é ', top3(n))
