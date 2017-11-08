def histograma(s):
    d=dict()
    for c in s:
        d[c]=d.get(c,0)+1
    return d

#print(histograma('banana'))


#2.

def print_hist(s):
    d=dict()
    for c in s:
        d[c]=d.get(c,0)+1
    k = list(d.keys())
    k.sort()
    for z in k:
        print(z, d[z])


#print_hist('banana')

#3.

def reverse_lookup(s,v):
    lista=[]
    d=dict()
    for c in s:
        d[c] = d.get(c,0)+1
    for l in d:
        if d[l] == v:
            lista.append(l)
    return lista
    raise ValueError

#print(reverse_lookup('banananbb',3))

#4.

def invert_dict(s):
    d = dict()
    inv = dict()
    for c in s:
        d[c] = d.get(c,0)+1
    for key in d:
        valor = d[key]
        inv.setdefault(valor,[]).append(key)
    return inv
        
    
print(invert_dict('ana'))

#5.

def tem_duplicados(l):
    d = dict()
    for s in l: 
        d[s]=d.get(s,0)+1
    for valor in d.values():
        if valor >1:
            return True
    return False

#print(tem_duplicados(['l','m','p']))

#6.
def chaves_words():
    d = dict()
    inv = dict()
    ficheiro = open('words.txt','r')
    line = ficheiro.readline()
    for line in ficheiro:
        word = line.strip()
        d[word] = len(word) 
    for key in d:
        valor = d[key]
        inv.setdefault(valor,[]).append(key)
    for key in inv:
        print('Tamanho:',key,'Número de palavras',len(inv[key]))
    print('Total de palavras:',len(d))
    

#chaves_words()

#7.

def mais_frequente(x):
    lista = []
    d = dict()
    for c in x:
        d[c] = d.get(c,0)+1
    valores = list(d.values())
    valores.sort(reverse=True)
    for v in valores:
        for k in d:
            if d[k] == v:
                if k not in lista:
                    lista.append(k)
    return lista

#print(mais_frequente('kkaaacjaaaaaaaaaaaaa'))

def mais_frequente(x):
    lista = []
    d = {}
    ficheiro = open(x)
    line = ficheiro.readline()
    for line in ficheiro:
        word = line.strip()
        for c in word:
            d[c] = d.get(c,0)+1
    valores = list(d.values())
    valores.sort(reverse=True)
    for v in valores:
        for k in d:
            if d[k] == v:
                if k not in lista:
                    lista.append(k)
    return lista

#print(mais_frequente('words.txt'))
        
    
    













    
    







