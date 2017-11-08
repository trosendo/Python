def conj_de_letras(str):
    letras=tuple(str)
    conj=[]
    for i in letras:
        if i not in conj:
            conj.append(i)
    return conj
