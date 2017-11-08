def dig_par(inf, sup):
    'função que verifica os numeros entre inf e sup em que todos os seus algarimos sao pares'
    if inf>9999 or inf<1000 or sup>9999 or sup<1000:
        print('Por favor introduza valores com 4 algarismos (entre 1000 e 9999)')
        return
    par=[]
    for i in range(inf, sup+1):
        tres=i//10
        dois=i//100
        um=i//1000
        if i%2==0:
            if tres%2==0:
                if dois%2==0:
                    if um%2==0:
                        par.append(i)
    return par
