def vogal(str):
    vogais='a, e, i, o, u, A, E, I, O, U'
    return str in vogais


def conta_vogais(str):
    vogal(str)
    c=0
    for i in range(0, len(str)):
        if vogal(str[i]):
            c+=1
    print(c)
