def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)


def factorial_i(n):
    result=1
    for i in range(1, n+1):
        result=result*i
    return result
    
