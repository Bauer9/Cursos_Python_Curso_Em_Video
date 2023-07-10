# tupla 
num = (2, 5, 9, 1)
# Lista
num2 = [2, 5, 9, 1]
num2 [2] = 3

print (num2)

num2.append(7)
print (num2)

num2.sort()
print (num2)

#inserir o valor Zero na posição 2
num2.insert(2, 0)
print (num2)

num2.pop()
print (num2)

num2.pop(2)
print (num2)

num2.remove(2)
print (num2)


if 2 in num2 :
    num2.remove(2)
    print (num2)
else :
    print ('Não achei o 2')

if 5 in num2 :
    num2.remove(5)
    print (num2)


num2.sort(reverse= True)
print (num2)

print (f'Essa lista tem {len(num2)}')


valores = []
valores.append(5)
valores.append(9)
valores.append(4)

print (valores)

for v in valores :  
    print (f'{v}...', end = '')

for c, v2 in enumerate(valores) :
    print (f'\nNa posição {c} encontrei o  valor {v2}!')   

print ('Cheguei ao final da lista.')

"""
valores2 = list ()
for cont in range ( 0, 5) :
    valores2.append ( int (input ('Digite o valor: ')))
print (valores2)

for c1, v3 in enumerate(valores2) :
    print (f'Na posição {c1} encontrei o valor {v3}!')   
"""

a = [2, 3, 4, 7]
b = a

print (a)
print (b)

a1 = [2, 3, 4, 7]
b1 = a1 # ligação
b1[2] = 8 # mudei só o B mas no Python quando uma lista é igual a outra o Python cria uma ligação entre as listas, mudou UMA, mudou as DUAS!!!!

print (f'Lista A1 {a1}')
print (f'Lista B1 {b1}')

a2 = [2, 3, 4, 7]
b2 = a2 [:]
b2[2] = 9 

print (f'Lista A2 {a2}')
print (f'Lista B2 {b2}')