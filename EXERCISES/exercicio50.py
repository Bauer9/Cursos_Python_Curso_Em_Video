# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

"""
num1 = int (input ('Digite um número: '))
num2 = int (input ('Digite um número: '))
num3 = int (input ('Digite um número: '))
num4 = int (input ('Digite um número: '))
num5 = int (input ('Digite um número: '))
num6 = int (input ('Digite um número: '))
"""


soma = 0
cont = 0
for c in range (1, 7) :
    num = int (input ('Digite o {} número: ' .format (c) ))
    if num % 2 == 0 :
        soma = soma + num
        cont += 1
    #soma = soma + num
    #cont += 1


#print ('Você informou {} números e a soma foi {}' .format (cont, soma))

print ('Você informou {} números PARES e a soma foi {}' .format (cont, soma))
#print ('A soma total dos números pares é {}: ' .format(num)) 
