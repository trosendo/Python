def prefixo_comum(s1,s2):
    if len(s1)>len(s2):
        s1, s2=s2, s1
    prefixo=''
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            prefixo+=s1[i]
        else:
            break
    return prefixo
                

def prefixo_comum_recursivo(s1,s2):
    if s1=='':
        return s1
    else:
        if s1 in s2:
            return s1
        return prefixo_comum_recursivo(s1[:len(s1)-1], s2)
