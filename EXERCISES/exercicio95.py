# Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

lista = list ()
jogador = dict ()
gols = list ()

while True :

    jogador ['nome'] = str (input ('Nome do jogador: '))
    jogador ['numeroPartidas'] = int (input (f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range (0, jogador ['numeroPartidas']) :
        #jogador['partidas'] = int (input (f'quantos gols na partida {i}? '))
        jogador ['numgols'] = int (input (f'Quantos gols na partida {i} ? '))
        #gols.append(numgols)
        #jogador['gols'] = (gols.copy())
        #jogador['totalGols'] = sum(gols)
        lista.append(jogador.copy())
        jogador.clear()
    gols.clear()
    pergunta = str (input ('Quer continuar? [S/N] ')).upper() [0]
    if 'N' in pergunta :
        break
    

print (gols)

print ('-=' * 30)
print (lista)
print ('-=' * 30)
#print (lista)


"""
for k, v in lista.items() :
    print (f'O campo {k}  tem o valor {v}')
    #print (f'O campo {jogador["nome"]} tem o valor {jogador["gols"]}')
print ('-=' * 30)
"""
"""
for k, v in enumerate (lista['gols']) :
    print (f'O jogador {jogador["nome"]} jogou {jogador["numeroPartidas"]} partidas.')
    print ('-=' * 30)
"""
    
    
"""
for k, v in enumerate (jogador['gols']) :
    print (f'Na partida {k}, ele fez {v} gols.')
    
    for v in jogador ['numeroPartidas'] :
        print (f'Na partida {k}, fez {v} gols.')
    
print (f'Foi um total de {jogador["totalGols"]} gols')
"""


