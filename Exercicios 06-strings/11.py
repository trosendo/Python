def ocorrencias_case(letra, string, indice):
    c=0
    dif=ord('a')-ord('A')
    string=string[indice:]
    c+=string.count(letra)
    if letra.isupper():
        c+=string.count(chr(ord(letra)+dif))
    else:
        c+=string.count(chr(ord(letra)-dif))
    print(c)

