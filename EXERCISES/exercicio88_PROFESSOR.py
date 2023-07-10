

from random import randint
from time import sleep # fazer que está levando um tempo para mostrar a informação

lista = list ()
jogos = list ()
print ('-=' * 30)
print ('-=' * 5, 'SORTEANDO', 'jogos' , 'JOGOS' , '-=' * 5)
print ('-=' * 30)
quant = int (input ( 'Quantos jogos você quer que eu sorteie? ' ))
tot = 1
while tot <= quant :
    count = 0
    while True :
        num = randint (1, 60)
        if num not in lista :
            lista.append (num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append (lista[:])
    lista.clear()
    tot += 1
#print (f'Os números sorteados foram {jogos}')

print ('-=' * 3, f'Sorteando {quant} jogos ', '-=' *3)
for i, l in enumerate (jogos) :
    print (f'jogo {i+1}: {l} ')
    sleep (1)
print ('-=' * 6, '< BOA SORTE! >', '-=' * 6)