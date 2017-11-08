def media(lista):
    c=0
    for i in lista:
       c=c+i
    media=c/len(lista)
    print('A média dos valores da lista é', media)

x=input('Insira uma lista de números(separados por vírgulas): ')
lista=list(eval(x))
media(lista)

