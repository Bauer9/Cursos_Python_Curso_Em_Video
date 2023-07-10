#Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict ()
gols = list ()
jogador ['nome'] = str (input ('Nome do jogador: '))
jogador ['numeroPartidas'] = int (input (f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range (0, jogador ['numeroPartidas']) :
    #jogador['partidas'] = int (input (f'quantos gols na partida {i}? '))
    numgols = int (input (f'Quantos gols na partida {i} ? '))
    gols.append(numgols)
    jogador['gols'] = (gols.copy())
    jogador['totalGols'] = sum(gols)

print (gols)

print ('-=' * 30)
print (jogador)
print ('-=' * 30)
for k, v in jogador.items() :
    print (f'O campo {k}  tem o valor {v}')
    #print (f'O campo {jogador["nome"]} tem o valor {jogador["gols"]}')
print ('-=' * 30)
print (f'O jogador {jogador["nome"]} jogou {jogador["numeroPartidas"]} partidas.')
print ('-=' * 30)

for k, v in enumerate (jogador['gols']) :
    print (f'Na partida {k}, ele fez {v} gols.')
    """
    for v in jogador ['numeroPartidas'] :
        print (f'Na partida {k}, fez {v} gols.')
    """
print (f'Foi um total de {jogador["totalGols"]} gols')

