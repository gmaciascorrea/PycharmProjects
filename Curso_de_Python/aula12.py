hora = input('Que horas são? ')

try:
    hora = int(hora)
    if hora >= 0 and hora < 11 :
        print('Bom dia!')
    elif hora >= 11 and hora < 17 :
        print('Boa tarde!')
    elif hora >= 18 and hora <=23 :
        print('Boa noite!')
    else: print('Digite uma hora válida seu pateta.')

except: print('Digite uma hora válida seu pateta.')
