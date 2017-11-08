def soma_todos({1, 2, 3}):
    if len(valores)==1:
        for i in valores:
            return i
    else:
        for i in valores:
            return soma_todos(i)+soma_todos(*valores[1:])


