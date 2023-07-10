# random de 4 alunos o professor qurr sortear um deles pelo nome

# randow = string(input('Digite o número'))
# num = random.randint(1,4)
# escolhido = num


""" MINHA SOLUÇÃO

import random

a1 =   str (input (' (1° jogador) Digite seu nome: '))
a2 =   str (input (' (2° jogador) Digite seu nome: '))
a3 =   str (input (' (3° jogador) Digite seu nome: '))
a4 =   str (input (' (3° jogador) Digite seu nome: '))

sort = random.randint(1,4)


if sort == 1:
    print ( 'Parabéns, {}, Você Ganhou!!' . format (a1) )
elif sort == 2:
    print ( 'Parabéns, {}, Você Ganhou!!' . format (a2))
elif sort == 3:
    print ( 'Parabéns, {}, Você Ganhou!!' . format (a3))
elif sort == 4:
    print ( 'Parabéns, {}, Você Ganhou!!' . format (a4))

"""

from random import choice

a1 =   str (input (' (1° jogador) Digite seu nome: '))
a2 =   str (input (' (2° jogador) Digite seu nome: '))
a3 =   str (input (' (3° jogador) Digite seu nome: '))
a4 =   str (input (' (3° jogador) Digite seu nome: '))

lista = [a1, a2, a3, a4]
# escolhido = random.choice(lista)
escolhido = choice(lista)
print ('O aluno escolhido foi {}' . format (escolhido))



# joao, carlos, antonio, maria


# print('O aluno sorteado agora é o de número: {}'.format(num))






