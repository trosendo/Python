segundos=int(input('Quantos segundos? '))

         
dias=(((segundos//60)//60)//24)

horas=((segundos//60)//60)-dias*24

minutos=((segundos//60))-dias*24*60-horas*60

segundos_resto=segundos-dias*24*60*60-horas*60*60-minutos*60

print(segundos, ' segundos corresponde a:') 

if (dias==1):
    print(dias, ' dia;')
else:
    print(dias, ' dias;')

if (horas==1):
    print(horas, ' hora;')
else:
    print(horas, ' horas;')

if (minutos==1):
    print(minutos, ' minuto;')
else:
    print(minutos, ' minutos;')

if (segundos_resto==1):
    print(segundos_resto, ' segundo;')
else:
    print(segundos_resto, ' segundos;')





