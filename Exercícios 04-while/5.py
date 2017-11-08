x=int(input('Qual o valor? '))
soma=0
count=0
if x!=0:
    soma+=x
    count+=1
    
while x!=0:
    x=int(input('Qual o valor? '))
    soma+=x
    if x!=0:
        count+=1

media=soma/count
print('Foram introduzidos ', count, ' valores e a média é ', media)
    
