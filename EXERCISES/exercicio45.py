# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
import random
from random import choice
from time import sleep
print ('{:=^40}' . format('JOKEMPÔ - PEDRA PAPEL E TESOURA'))


print ('''Escolha:
[ 0 ] Pedra 
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int (input ( 'Qual a sua jogada? ' ))
#if opcao >3 :
 #   print ('OPÇÃO INVÁLIDA!')

   



#lista = ['pedra', 'papel', 'tesoura']
itens = ('Pedra' , 'Papel' , 'Tesoura')
# escolhido = random.choice(lista)
#computador = choice(lista)
computador = randint(0, 2)

print ('Você escolheu {} ' .format (itens [jogador] ))


print ('JO') 
sleep (1)
print ('KEN') 
sleep (1)
print ('PO') 
sleep (1)

print ( '=' * 31 )
print ('Computador jogou: {}' . format ( itens [computador]))
print ('Você jogou: {}' .format ( itens [jogador]))
print ( '=' * 31 )


if  jogador == 0 :
    if computador == 0 :
        print ('Empatou!')
    elif computador == 1 :
        print ('Você Perdeu!')
    elif computador == 2 :
        print ('Você Ganhou!')
    else :
        print ('Jogada invalida!')

if  jogador == 1 :
    if computador == 0 :
        print ('Você Ganhou!')
    elif computador == 1 :
        print ('Empatou!')
    elif computador == 2 :
        print ('Você Perdeu!')
    else :
        print ('Jogada invalida!')

if  jogador == 2 :
    if computador == 0 :
        print ('Você Perdeu!')
    elif computador == 1 :
        print ('Você Ganhou!')
    elif computador == 2 :
        print ('Empatou!')
    else :
        print ('Jogada invalida!')

print ('')


"""
1 = pedra
2 = tesoura
3 = tesoura
"""

"""
if jogador == 1 :
    jogador = 'pedra'
elif jogador == 2 :
    jogador = 'papel'
elif jogador == 3 :
    jogador = 'tesoura'
    
"""     

"""
if  jogador == 'pedra' :
    if computador == 'pedra' :
        print ('Empatou!')
    elif computador == 'papel' :
        print ('Você Perdeu!')
    elif computador == 'tesoura' :
        print ('Você Ganhou!')
    else :
        print ('Jogada invalida!')

if  jogador == 'papel' :
    if computador == 'pedra' :
        print ('Você Ganhou!')
    elif computador == 'papel' :
        print ('Empatou!')
    elif computador == 'tesoura' :
        print ('Você Perdeu!')
    else :
        print ('Jogada invalida!')

if  jogador == 'tesoura' :
    if computador == 'pedra' :
        print ('Você Perdeu!')
    elif computador == 'papel' :
        print ('Você Ganhou!')
    elif computador == 'tesoura' :
        print ('Empatou!')
    else :
        print ('Jogada invalida!')

print ('')
"""

