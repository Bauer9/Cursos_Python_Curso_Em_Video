temp = list ()
princ = []

mai = men = 0

while True :
    temp.append (str(input('Nome: ')))
    temp.append (float(input ('Peso: ')))
    if len(princ) == 0 :
        mai = men = temp[1]
    else:
        if temp[1] > mai :
            mai = temp[1]
        if temp[1] < men :
            men = temp[1]

    princ.append (temp[:])
    temp.clear()
    resp = str (input ('Quer continuar? [S/N]:')).strip().upper()
    if resp == 'N' :
        break   

print ('-=' * 25)
print (f'Temp: {temp}')
print (f'Principal: {princ}')
print (f'Ao todo vc cadastrou: {len(princ)} pessoas.')
print (f'Menor peso: {men}Kg. Peso de ', end = '')
for p in princ :
    if p[1] == men :
        print (f'[{p[0]}] ', end = '')
print ( )
print (f'Maior peso: {mai}Kg. Peso de ', end = '')
for p in princ :
    if p[1] == mai :
        print (f'[{p[0]}] ', end = '')

print ( )