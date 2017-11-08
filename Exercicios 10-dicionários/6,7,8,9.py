dicEnPt= {'white':'branco', 'the':'o', 'cat':'gato', 'mouse':'rato',
'chases':'persegue', 'black':'preto' }

def traduz(pal, dic):
    for i in dic.keys():
        if i==pal:
            return dic[i]
    return pal


def palavra_para_portugues(pal):
    dicEnPt= {'white':'branco', 'the':'o', 'cat':'gato', 'mouse':'rato', 'chases':'persegue', 'black':'preto' }
    return traduz(pal, dicEnPt)


def lista_para_portugues(lista_pals):
    lista=[]
    for pal in lista_pals:
        lista.append(palavra_para_portugues(pal))
    return lista


def frase_para_portugues(frase):
    frase_pals=frase.split()
    lista=lista_para_portugues(frase_pals)
    traduzido=' '.join(lista)
    return traduzido
    
