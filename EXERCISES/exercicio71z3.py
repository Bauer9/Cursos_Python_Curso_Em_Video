

print ('=' * 31)
print (' ' *5,' BANCO CEV', ' ' *5)
print ('=' * 31)

valor =  int (input ('Quanto você quer sacar: '))

total = valor
ced = 50
totced = 0

while True :
    if total >= ced :
        total -= ced
        totced += 1
    else :
        if totced > 0 :
            print (f'Total de {totced} cédulas de {ced}')
        if ced == 20 :
            total = total - 20
            torced += 1
        if total == 0 :
            break



print ('Volte sempre ao BANCO CEV! Tenha um bom dia!')


