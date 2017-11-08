def consulta_preço(artigo, tabela):
    for i in tabela:
        if artigo in i:
            return i[1]


def artigo_mais_caro(tabela):
    preços=[]
    for i in tabela:
        preços.append(i[1])
    preços.sort()
    mais_caro=preços[len(preços)-1]
    print(mais_caro)
    for i in tabela:
        if mais_caro in i:
            return i[0]
