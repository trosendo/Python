def palindromo(str):
    str_inv=''
    for i in range(1, len(str)+1):
        str_inv=str_inv+str[len(str)-i]
    if str==str_inv:
        return True
    else:
        return False
