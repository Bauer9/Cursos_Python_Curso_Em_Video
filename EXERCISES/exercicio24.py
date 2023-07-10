# crie um programa que leia o nome da Cidade
# e ele diga se ela começa ou não com a palavra "SANTO"
# 
# 


cid = str(input('Em que cidade você nasceu? ')).strip() .upper()

"""
res = cid.lower() 

res1 = cid.count('santo')

#res = resultado
# resultado = 1

print ('a cidade {} começa com Santo'.format(res1))

"""

print (cid[:5] == 'SANTO')


