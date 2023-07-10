# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


# MINHA SOLUÇÃO
soma = 0
quantidade = 0
num = 0
while num != 999 :
    
    soma = soma + num 

    num = int (input ('Digite um número [999 para parar]: '))
    if num != 999 :
        quantidade += 1



print ('Você digitou {} números e a soma entre eles foi {}' .format (quantidade, soma))
#print ('Acabou 1')


"""
# SOLUÇÃO PROFESSOR 
soma = 0
quantidade = 0
num = 0
num = int (input ('Digite um número [999 para parar]'))
while num != 999 :
    soma = soma + num 
    quantidade += 1
    num = int (input ('Digite um número [999 para parar]'))
    

#print ('Acabou 1')
"""




