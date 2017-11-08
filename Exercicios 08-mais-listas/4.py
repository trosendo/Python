def ordena(s):
    s=s.replace(' ', '')
    s=s.split(',')
    
    ordena=[]
    
    while s:
        maximo = s[0]  
        for x in s: 
            if x<maximo:
                maximo = x
        ordena.append(maximo)
        s.remove(maximo)    

    print(ordena)
