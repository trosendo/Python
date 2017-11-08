h=float(input('Qual a altura da pessoa? '))

if h<1.3:
    true='baixíssima'
elif h>=1.3 and h<1.6:
    true='baixa'
elif h>=1.6 and h<1.75:
    true='mediana'
elif h>=1.75 and h<1.9:
    true='alta'
else:
    true='altíssima'

print('Essa pessoa é ', true)
