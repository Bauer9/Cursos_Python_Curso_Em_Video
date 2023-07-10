# quer sortear um programa que le o nome dos 4 alunos e colocar em ordem de apresentação



from random import shuffle


a1 =    str (input (' (1 jogador) digite seu nome '))
a2 =    str (input (' (2 jogador) digite seu nome '))
a3 =    str (input (' (3 jogador) digite seu nome '))
a4 =    str (input (' (4 jogador) digite seu nome '))

lista = [a1, a2, a3, a4]

shuffle(lista)


print ('A ordem de apresentação será')
print (lista)





