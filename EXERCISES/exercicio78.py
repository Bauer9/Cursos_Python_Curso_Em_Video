# add 5 valores númericos em uma lista e leia eles
# maior e menor valor e suas posições na Lista

menor = 0
maior = 0
lista1 = []

print ('=-' * 30)
for c in range (0, 5) :
    lista1.append (int (input ('digite um número: ')))
    if c == 0 :
        menor = maior = lista1[c]
    else: 
        if lista1[c] > maior :
            maior = lista1[c]
        if lista1[c] < menor :
            menor = lista1[c]


print (f'A lista contem: {lista1}')


# MINHA RESOLUÇÃO
if menor in lista1 :
    index = lista1.index(menor)
    #print (f'O menor {menor} está nas posições: {lista1.index(menor)}', end = '')    
    print (f'O menor {menor} está nas posições: ', end = '')    

#PROFESSOR
for i, v in enumerate (lista1) :
    if v == menor :
        print (f'{i}..., ', end = '')
print ( )
if maior in lista1 :
    index = lista1.index(maior)
    #print (f'O maior {maior} está nas posições: {lista1.index(maior)}', end = '')        
    print (f'O maior {maior} está nas posições: ', end = '')    

#PROFESSOR
for i, v in enumerate (lista1) :
    if v == maior :
        print (f'{i}..., ', end = '')
print ( )

    

# INTERNET 
"""
from collections import Counter
c = Counter(lista1)

for numero, repeticoes in c.items():
    if repeticoes > 1:
        result = [indice for indice, item in enumerate(lista1) if item == numero]
        print(f'O número "{numero}" se repete nos índices {result}.')
"""

# PROFESSOR
