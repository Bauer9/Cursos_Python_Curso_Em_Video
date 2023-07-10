"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""

from random import randint
from time import sleep

"""
def sorteia (numeros) :
    for num in range (0, 5) :
        num = randint(0, 11)
        numeros.append(num)

#print (num)

#print (numeros)


def somaPar (numeros) :
    num1 = 0
    if num1 % 2 == 0 :
        pares.append(num1)
        print (sum (pares))
        print (pares)

numeros = list ()
pares = list ()
sorteia (numeros)
somaPar (numeros)
print (numeros)
print (pares)

"""

#"""
def sorteia (lista) :
    print ('Sorteando 5 valores da lista: ', end = '')
    for cont in range (0, 5) :
        n = randint (1, 10)
        lista.append(n)
        print (f'{n} ', end = '')
        sleep (0.3)
    print ('Pronto!')


def somaPar (lista) :
    soma = 0
    for valor in lista :  
        if valor % 2 == 0 :
            soma += valor
    print (f'Somando os valores pares de {lista}, temos {soma}')

#"""
numeros = list ()
sorteia (numeros)
somaPar (numeros)


