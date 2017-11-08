import math
def raiz2(a, x, epsilon):
    while True:
        y = (x+a/x)/2
        if abs(y-x)<epsilon:
            break
        x = y
    return y

def test_sqrt(a, x):
    num1=float(raiz2(a, x, 0.0001))
    num2=float(math.sqrt(a))
    dif=abs(num1-num2)
    print('raiz2=', num1)
    print('math.sqrt=', num2)
    print('diferença=', dif)

