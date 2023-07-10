#


n = 0
cont = 0
soma = 0
while n != 999:
    n = int (input ('Digite um número: '))

    if n == 999 :
        break

    cont += 1

    #if n != 999 :
    soma = soma + n



#print ('A soma vale {}' .format (soma))
print (f'Você digitou {cont} números e a soma deles é {soma}') # nova forma para o Python 3.06 para cima
print ('Acabou')
