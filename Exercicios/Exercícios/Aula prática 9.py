def sort_by_length_random(x):
    from random import choice
    lista = []
    d = dict()
    for word in x:
        if len(word) in d:
            d[len(word)].append(word)
        else:
            d[len(word)] = [word]
    objectos = list(d.keys())
    objectos.sort(reverse=True)
    for l in objectos:
        while len(d[l]) > 0:
            escolha = d[l].pop(choice(range(0,len(d[l]))))
            lista.append(escolha)
    return lista
        
            

##print(sort_by_length_random(['um','dois', 'três', 'quatro', 'asa', 'casa', 'quintal']))

#2.

def filtro_por_tamanho():
    tuplos = []
    lista = []
    ficheiro = open('words.txt')
    line = ficheiro.readline()
    for line in ficheiro:
        word = line.strip()
        tuplos.append((word,len(word)))
    x = int(input('Insira inteiro para filtrar:'))
    for tuplo in tuplos:
            if tuplo[1] == x:
                lista.append(tuplo[0])
    print('Número de palavras filtradas:', len(lista))
    z = input('Deseja ver as palavras filtradas(s/n):')
    if z == 's':
        for word in lista:
            print()
            print(word)
    else:
        import sys
        sys.exit()

##filtro_por_tamanho()
            

#3.
def process_file(x):
    import string
    import bisect
    from random import choice
    ficheiro = open(x)
    d = {}
    palavra = []
    separadores = list(string.punctuation)
    adicionar = [' ','«','»','“','”']
##    abc = list(string.ascii_lowercase)
##    numbers = list(string.digits)
    for x in adicionar:
        separadores.append(x)
    line = ficheiro.readline()
    for line in ficheiro:
        frase_normal = line.strip()
        frase_min = frase_normal.lower()
        for c in frase_min:
            if c in separadores:
                word = ''.join(palavra)
                d[word] = d.get(word,0)+1
                palavra = []
            else:
                palavra.append(c)
##    for key in d.keys():
##        print(key)
    valores = d.values()
    soma = []
    s = 0
    for v in valores:
        s+=v
        soma.append(s)
    r = choice(range(0,soma[len(soma)-1]))
    index = bisect.bisect(soma,r)
    return(index)
    
    
##print(process_file('notícia.txt'))
        
        

#print(random_words('A aula de programação é em Python'))

#4.
def lista_de_palavras(x):
    import string
    ficheiro =  open(x)
    prefixos = {}
    line = ficheiro.readline()
    palavras = []
    separadores = list(string.punctuation)
    adicionar = [' ','«','»','“','”']
    for x in adicionar:
        separadores.append(x)
    for line in ficheiro:
        line = line.strip().lower()
        for c in line:
            if c in separadores:
                line = line.replace(c,' ')
        linha = line.split(' ')
        for word in linha:
            if word != '':
                palavras.append(word) 
    return (palavras)

def markov(x):
    palavras = lista_de_palavras(x)
    start = 0
    end = 2
    mapa = {}
    while end <= len(palavras)-2:
        prefixos = tuple(palavras[start:end])
        sufixo = palavras[end]
        lista = []
        lista.append(sufixo)
        mapa[prefixos] = mapa.get(prefixos,[]) + lista
        start +=1
        end +=1
    return mapa

def random_text(x,y):
    from random import choice
    análise = x
    for palavra in range(y):
            random_word = choice(list(análise.keys()))
            prefixos = ' '.join(random_word)
            sufixo = ''.join(choice(análise[random_word]))    
            print()
            print(prefixos)
            print()
            print(sufixo)
##            prefixos = (random_word[1],sufixo)
##            sufixos = ''.join(choice(análise[(random_word[1],sufixo)]))
            

##random_text(markov('notícia.txt'),2)
                
