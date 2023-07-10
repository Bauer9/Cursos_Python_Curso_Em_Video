# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar 
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
from random import randint
from time import sleep # fazer que está levando um tempo para mostrar a informação


#c = 0

quantJogos = int (input ( 'Quantos jogos você quer que eu sorteie? ' ))

print ('-=' * 5, f'SORTEANDO, {quantJogos}, JOGOS' , '-=' * 5)
matriz = [[random], [random], [random], [random], [random], [random]]

c=0
jogos = list ()
jogosAll = list ()
tot = 1
while  c <= quantJogos :
    count = 0 
    while True :
        num = randint(1,60)
        if num not in jogos :
            jogos.append (num)
            count += 1
        if count >= 6 :
            break
    jogos.sort()
    jogosAll.append (jogos[:])
    jogos.clear()
    tot += 1

#print (f'Jogo {c+1}:', jogos)

#print ('-=' * 6, '< BOA SORTE! >', '-=' * 6)


print ('-=' * 3, f'Sorteando {quantJogos} jogos ', '-=' *3)
for i, l in enumerate (jogosAll) :
    print (f'jogo {i+1}: {l} ')
    sleep (1)
print ('-=' * 6, '< BOA SORTE! >', '-=' * 6)


