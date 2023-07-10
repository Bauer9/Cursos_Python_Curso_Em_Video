# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

"""
a1 =    str (input (' (1 jogador) digite seu nome '))
a2 =    str (input (' (2 jogador) digite seu nome '))
a3 =    str (input (' (3 jogador) digite seu nome '))
a4 =    str (input (' (4 jogador) digite seu nome '))

lista = [a1, a2, a3, a4]
"""
somaidade = 0
idademedia = 0
mulheresmenosde20 = 0 
maioridadeM = 0
idadeF = 0
nomeM = 0

for p in range (1, 5) :
    print ('---- {} PESSOA -----' .format(p))
    nome = str (input ('Digite o nome da {} pessoa: '  .format(p))) .strip().upper()
    idade = int (input ('Digite a idade da {} pessoa: ' .format(p)))
    sexo = str (input ('Digite o sexo da {} pessoa [M/F]: ' .format(p))) .strip().upper()
    somaidade = somaidade + idade
    if sexo == 'M' :
        if idade > maioridadeM :
            maioridadeM = idade
            nomeM = nome
    if sexo == 'F' :
        if idade < 20 :
             mulheresmenosde20 += 1
    

mediaidade = somaidade /4

print ('A média de idade do grupo é de {:.2f} anos'.format(mediaidade))
print ('O homem mais velho tem {} anos e se chama {}' .format (maioridadeM, nomeM))
print ('Ao todo são {} mulheres com menos de 20 anos' .format ( mulheresmenosde20 ))






