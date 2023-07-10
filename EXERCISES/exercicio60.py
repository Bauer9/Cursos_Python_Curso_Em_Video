# Faça um programa que leia um número qualquer e mostre o seu fatorial.
""" Modo rápido e facil
from math import factorial
f = factorial (num)
print ('O fatorial de {} é: {}' .format(num, f))
"""


num = int (input ('Digite um número para Calcular o fatorial: '))

cont = 1
next = 0
result = 1
print ('Calculando {}! = {}' .format (num, num), end = '')
while cont < num :
    next = num - 1
    print (' x {}' .format(next), end = '')
    result = result * num
    num = next


print (' = {}' .format(result))
print ('FIM')
