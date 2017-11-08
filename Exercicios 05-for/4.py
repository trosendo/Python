n=int(input('Qual o numero? '))
c=n
while n<0:
    n=int(input('Qual o numero? '))
    c=n
if n==0:
    print(1)
else:
    for i in range(1, c):
        n=n*(c-i)
    print(n)

