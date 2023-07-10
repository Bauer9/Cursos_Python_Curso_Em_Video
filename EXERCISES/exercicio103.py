""" 
Faça um programa que tenha uma função chamada ficha(), 
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.
"""
"""
def ficha (nome, gols) :
    print ('-=' * 30)
    if len(nome) == 0 :
        print (f'O jogador desconhecido fez {gols} gol(s) no campeonato')
    elif len(gols) == 0 :
        print (f'O jogador {nome} fez 0 gol(s) no campeonato') 
    elif len(nome) == 0 and len(gols) == 0 :
        print (f'O jogador desconhecido fez 0 gol(s) no campeonato')
    else:
        print (f'O jogador {nome} fez {gols} gol(s) no campeonato')
"""

""" # MINHA RESOLUÇCÃO 1
def ficha (nome, gols) :
    print ('-=' * 30)
    if len(nome) == 0 or len(gols) == 0 :

        if len(nome) == 0 and len(gols) > 0 :
            print (f'O jogador desconhecido fez {gols} gol(s) no campeonato')
        elif len(gols) == 0 and len(nome) > 0 :
            print (f'O jogador {nome} fez 0 gol(s) no campeonato') 
        elif len(nome) == 0 and len(gols) == 0 : 
            print (f'O jogador desconhecido fez 0 gol(s) no campeonato')    
            
        
    elif len(nome) > 0 and len(gols) > 0:
        print (f'O jogador {nome} fez {gols} gol(s) no campeonato')
    print ('-=' * 30)
"""
#ficha (nome, gols)

nome = str (input ('Figite o nome do jogador: ')).strip()
gols = str (input ('Quantos gols o jogador fez? ')).strip()

# PROFESSOR
def ficha (nome = '<desconhecido>', gols = 0) :
    print ('-=' * 30)
    print (f'O jogador {nome} fez {gols} gol(s) no campeonato')
    print ('-=' * 30)

if gols.isnumeric() : 
        gols = int (gols)
else:
    gols = 0
if nome.strip() == '' : 
    ficha(gols=gols)
else:
    ficha(nome, gols)




