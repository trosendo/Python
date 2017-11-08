def capicua(numero):
    while len(numero) != 3:
        print("O numero ", numero, "não tem 3 digitos!")
        numero = (input("Indique um número de 3 algarismos: "))
    if numero[0] == numero[2]:
        print("O numero ", numero, "é capicua!")                  
    else:
        print("O numero ", numero, "não é capicua!")
    
numero1 = (input("Indique o 1º número de 3 algarismos: "))
capicua(numero1)

numero2 = (input("Indique o 2º número de 3 algarismos: "))
capicua(numero2)
