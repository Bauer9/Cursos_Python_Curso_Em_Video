"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, 
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""



lista = ('Lápis', 5.00,
         'Caneta', 10.00,
         'Caderno', 25.00,
         'Mochila', 120.00,
         'çompasso', 180.00)



print ('_' * 40)
print (f'{"LISTAGEM DE PREÇOS":^40} ') # centralizar texto :^40
print ('_' * 40)
"""
for pos in range (0, len(lista)) :
    print (lista[pos])


"""

for pos in range (0, len(lista)) :
    if pos % 2 == 0 :
        print (f'{lista[pos]:.<30}', end ='')
    else:
        print (f'R${lista[pos]:>7.2f}')


print ('_' * 40)





