"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
import random


jogadores = dict ()

for j in range (1, 5) :
    print (f'Jogador {j} tirou {randint(1, 6)} ')
    jogadores.append()

print ('-=' * 30)

print ('== RANKING DOS JOGADORES ==')






"""
print (f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print ('-' *26)
for i, a in enumerate (boletim) :
    print (f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
"""