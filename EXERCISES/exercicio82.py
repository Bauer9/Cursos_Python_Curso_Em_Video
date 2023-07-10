# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.


lista = list () # ou lista = []
pares =  list ()
impares =  list ()
"""
while True :
    num = int (input ('Digite um valor: '))
    lista.append (num)

    if num % 2 == 0 :
        pares.append (num)
    elif num % 2 != 0: 
        impares.append (num)

    continuar = str (input ('Quer continuar? [S/N]: ')).strip().upper()
    if continuar in 'N' :
        break    


    #continuar = 'a'
    #while continuar not in "SN" :
    #    continuar = str (input ('Quer continuar? [S/N]: ')).strip().upper()
    #    if continuar in 'N' :
    #        break
    #    elif  continuar not in 'SN' :
    #        print ('Resposta invalida!')  


print ('=-' * 20)
lista.sort()
print ( f'A lista completa é: {lista}' )
pares.sort()
print ( f'A lista de pares é: {pares}' )
impares.sort()
print ( f'A lista de ímpares é: {impares}' )
"""

# PROFESSOR
lista2 = list () # ou # lista 2 = []
while True :
    lista2.append (int (input ('Digite um valor: ')))
    resp = str (input ('Quer continuar? [S/N]: ')).strip().upper()
    if resp in 'N' :
        break

for i, v in enumerate (lista2) :
    if v % 2 == 0 :
        pares.append (v)
    elif v % 2 == 1 : # ou #     elif v % 2 != 0 :
        impares.append (v)

print ('x-' * 20)
lista2.sort()
print ( f'A lista completa é: {lista2}' )
pares.sort()
print ( f'A lista de pares é: {pares}' )
impares.sort()
print ( f'A lista de ímpares é: {impares}' )
