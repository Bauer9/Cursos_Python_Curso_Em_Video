"""
Faça um programa que tenha uma função chamada contador(), 
que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""

from time import sleep

def contador (inicio, fim, passo): 
    print ('Imprimindo: ', end = '', flush = True)
    sleep(.5)
    
    if passo < 0 :
        passo *= -1
    
    if fim < inicio :
        passo = - passo
        
    if passo == 0 :
        passo = 1
        
    for c in range (inicio, fim+1 , passo) :
        print (f'{c}', end = ', ', flush = True)

# PROGRAMA PRINCIPAL
print ('-=' * 30)
contador (1, 10, 1)
print ('\n','-=' * 30)
contador (10, 0, 2)
print ('\n')
print ('-=' * 30)


print ()
print ('-' * 30)
inicio = int (input ('inicio: '))
fim = int (input ('fim: '))
passo = int (input ('passo: '))
print ('-' * 30)

contador (inicio, fim, passo)



