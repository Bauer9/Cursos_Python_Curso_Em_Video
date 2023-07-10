# 
# 
# l

# comando para sair de um looping - "break"


"""


cont = 1
while cont <= 10 :
    print (cont, '-> ', end = '' )
    cont +=1

    print ('Acabou')

"""


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
print (f'A soma vale {soma:.2f}') # nova forma para o Python 3.06 para cima
print ('Acabou')



"""
cont = 1
while True :
    print (cont, '-> ', end = '' )
    cont +=1

    print ('Acabou')

"""
