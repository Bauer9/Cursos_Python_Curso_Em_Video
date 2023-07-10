# Estrutura de repetição while - Laços

# WHILE
"""




while not ?:


c=1 
while c !=10:

    print(c)

    c+=1

print ('Acabou')

"""


numeros = 0
par = inpar = 0
valor = 1
while valor != 0 :
    valor = int (input ('Digite o valor: '))
    #print (valor)
    if valor % 2 == 0:
        par += 1
        numeros += 1
    else:
        impar =+ 1
        numeros += 1
print ('Valor = 0, Acabou2')
print ('Dos números {} são par e {} são impar.' .format(par, impar))
print ('Você digitou {} números' .format (numeros))







