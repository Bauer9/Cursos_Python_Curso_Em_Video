"""
Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
"""


maior18 = 0
numHOMENS = 0
Mmenor20 = 0

print ('-' * 20)
print ('CADASTRE UMA PESSOA')
print ('-' * 20)

while True :


    idade = int (input ('Qual a idade: '))

    sexo = ' '
    while sexo not in 'MF'  :
        sexo = str (input ('Qual o sexo Masculino ou Feminino [M/F]: ')).strip().upper()[0]

    if idade > 18: 
        maior18 += 1

    if sexo == 'F' :
        if idade < 20 :
            Mmenor20 += 1

    if sexo == 'M' :
        numHOMENS += 1


    #print (f'numHOMENS {numHOMENS}')

    continuar = ' '
    while continuar not in 'SN'  :
        continuar = str (input ('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N' :
        break

print (f'Pessoas com mais de 18 anos {maior18}')
print (f'Foram cadastrados {numHOMENS} homens')
print (f'Mulheres que tem menos de 20 anos {Mmenor20}')


