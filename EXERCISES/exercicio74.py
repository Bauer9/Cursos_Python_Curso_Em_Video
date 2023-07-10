from random import randint
import random

contador = 0
"""
for c in range (0, 5) :
    lista = computador = randint(0, 10)
    c+=1

while contador <= 5 :
    lista = randint(0, 10)
    contador += 1
    print (lista)
    #print (sorted(lista))
"""

#lista = tuple(randint (0, 10) for c in range (0, 5)) 

#print (lista)

#minha_tupla = tuple(random.randint(0, 100) for _ in range(5))


"""
lista2  = random.sample(range(0,100), 4)
print (lista2)
"""
#a


"""

# MINHA SOLUÇÃO
lista3 = tuple (random.sample (range (0, 10), 5) )
#print (lista3)

#sorted(lista3)
print (f'Os números sorteados foram : {lista3}')
print (sorted(lista3)) 
print ('O menor número é: ', sorted(lista3)[0])
print ('O maior número é: ', sorted(lista3)[4])

"""

# PROFESSOR
numeros =(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print (f'Os números sorteados foram : {numeros}')
for n in numeros :
    print (f'{n} ', end = '')


#print (sorted(numeros)) 
print (f'\nO menor número é:  {sorted(numeros)[0]}')
print (f'O maior número é:  {sorted(numeros)[4]}')
