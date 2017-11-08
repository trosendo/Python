def right_justify(s):
    espaços=70-len(s)
    s1=espaços*' '
    s2=s1+s
    print(s2)
    return;

s=str(input('Escreva qualquer coisa: '))
right_justify(s)
    
