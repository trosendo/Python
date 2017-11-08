def vogal(c):
    vogais=['a', 'e', 'i', 'o', 'u']
    for i in vogais:
        if c == i:
            return True
        return False

def conta_vogais(frase):
    if frase=='':
        return 0
    else:
        x=conta_vogais(frase[1:])
        print(x)
        if vogal(frase[0]):
            x=x+1
        return x

scan = input()
conta_vogais(scan)
