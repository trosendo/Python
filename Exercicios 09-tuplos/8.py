# jogos=[("ana","rui"),("manuel","maria"),("rita","joel")]
# resultados=[(2,0),(1,3),(1,1)]

def nome_vencedores(jogos, resultados):
    listav=[]
    for i in range(len(jogos)):
        jogo_atual=(jogos[i][0],resultados[i][0]),(jogos[i][1],resultados[i][1])
        if jogo_atual[0][1]>jogo_atual[1][1]:
            listav.append(jogo_atual[0][0])
        elif jogo_atual[0][1]<jogo_atual[1][1]:
            listav.append(jogo_atual[1][0])
        else:
            listav.append('EMPATE')
    return listav
