def rot13(str):
    'Para palavras com maisuculas e minusculas'
    str_codded=''
    for c in str:
        if ord(c)<=77 and c.isupper() or ord(c)<=109 and c.islower():
            str_codded+=chr(ord(c)+13)
        else:
            str_codded+=chr(ord(c)-13)
    print(str_codded)



        
