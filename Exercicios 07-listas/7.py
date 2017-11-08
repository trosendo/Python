def combina(pals1, pals2):
    'Propriedade distributiva entre strings em listas'
    string=[]
    x=0
    for i in range(len(pals1)):
        for c in range(len(pals1)):
            string.append(pals1[i]+' '+pals2[c])
            print(string[x])
            x+=1
        
        
