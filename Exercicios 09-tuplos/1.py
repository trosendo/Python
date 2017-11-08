def consulta_preço(artigo, tabela):
    for i in tabela:
        if artigo in i:
            return i[1]


def artigo_mais_caro(tabela):
    maximo=tabela[0][1]
    mais_caro=()
    for i in range(len(tabela)):
        if tabela[i][1]>maximo:
            mais_caro+=(tabela[i][0], tabela[i][1])
    print(mais_caro[-2:])
