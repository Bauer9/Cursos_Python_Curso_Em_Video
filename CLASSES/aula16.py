
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

#lanche[1] = 'cocacola' # erro, não dá para mudar o conteúdo de Tuplas

"""
print (lanche)

print (lanche[1])

print (lanche[-1])
print (lanche[-2])
print (lanche[-3])
print (lanche[-4])

print (lanche[-2:])

print (lanche[0:2])
print (lanche[:2])
"""
#print (lanche[1])


#print (len(lanche))

for cont in range (0, len(lanche)) :
    #print (cont)
    print (f'Eu vou comer {lanche[cont]}')

print ('Outra Opção')

# for
for comida in lanche :
    print (f'Eu vou comer {comida}')

print ('Comi para caramba!')

for cont in lanche :
    print (f'Eu vou comer {cont}')

print ('Comi para caramba!')

for cont in range (0, len(lanche)) :
    #print (cont)
    print (f'Eu vou comer {lanche[cont]} na posição {cont}')

for cont in enumerate (lanche) :
    print (f'Eu vou comer {cont}')

print ('Comi para caramba!')

for pos, cont in enumerate (lanche) :
    print (f'Eu vou comer usando o enumerate {cont} na posição {pos}')

print ('Comi para caramba!')

print (' ')

print (sorted(lanche)) # cria uma nova lista para ordenar a Tupla
print (lanche)

print (' ')


a = ( 2, 5, 4)
b = (5, 8, 1, 2)
d = a + b
c = b + a
print (c)
print (d)
print (len(c)) # conta quantos elementos tem na Tupla C

print (c.count(5)) # quantas vezes o número 5 aparece dentro de C

print (c)
print (c.index(8)) # posição do 8 dentro da Tupla, ela começa com 0/Zero

print (c.index(2)) # só mostra a primeira posição do 2, ele ignora o segundo 2
print (c.index(2, 4)) # começa a contar a partir da posição 1 e assim monstra a posição do segundo 2

pessoa = ('Gustavo', 39, 'M', 99.88) # no Java e outras linguagens a Tupla só aceita o mesmo tipo de elementos, no Python não, ele aceita nomes, números, etc

#del (pessoa) # apagar a Tupla inteira é possível

print (pessoa)



