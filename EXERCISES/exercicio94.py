"""
Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 

No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""

lista = list () 
pessoas = dict () # pessoas = {}  ?
contF = 0

mediaIdade = 0
sunIdade = 0 
while True :
    pessoas['nome'] = str (input ('Nome: '))
    pessoas['sexo'] = str (input ('Sexo: [M/F] ')).strip().upper()
    pessoas['idade'] = int (input ('Idade: '))
    lista.append(pessoas.copy())
    
    #mediaIdade.append(pessoas['idade'])
    #mediaIdade.append(pessoas["idade"])
    print (f'a média de idade 1 é: {mediaIdade}+1')
    #mediaIdade = (sum(pessoas['idade']) ) / (len(lista)-1)
    print (f'a média de idade 2 é: {mediaIdade}')
    
    if pessoas['sexo'] == 'F' :
        contF += 1
    #print (pessoas['idade'])
    #print (mediaIdade)

    while True :
        pergunta = str (input ('Quer continuar [S/N]: ')).strip().upper()
        if pergunta == 'S' :
            break
        elif pergunta != 'SN' :
            print ('ERRO! Responda apenas S ou N')
        
        if pergunta == 'N' :
            break

    mediaIdade = pessoas['idade'] / len(pessoas)+1
    
    if pergunta == 'N' :
            break   


#mediaIdade = (pessoas['idade']) / (len(lista)-1)
#print (f'a média de idade é: {mediaIdade}')


print ('-=' * 30)            
print (pessoas)
print (lista)
print ('-=' * 30)
print (f'A) Ao todo temos {len(pessoas)-1} pessoas cadastradas')
#print (f'B) a média de idade é {mediaIdade} anos')
print (f'C) As mulheres cadastradas foram {contF} ')
print ('D) Lista das pessoas que estão acima da idade média:')

for k, v in enumerate (lista) :
    print (f'   O nome: {k}, e idade: {v}')
    
"""
for k, v, i in lista :
    print (f'{k} = {lista["nome"]}; {v}; {i};')
    #print (f'{lista["nome"]}; {lista["sexo"]}; {pessoas["idade"]};')
"""
print ('<< ENCERRADO >>')








