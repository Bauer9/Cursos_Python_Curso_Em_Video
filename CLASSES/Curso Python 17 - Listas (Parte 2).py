#Listas dentro de Listas

dados = list () # ou dados = []


dados.append(Pedro) # add Pedro no final da lista
dados.append(25) # add 25 na lista

print (dados[0]) 
# Pedro

print (dados[1])
# 25

pessoas = lista()
pessoas.append(dados[:]) #criei uma lista pessoas que dentro tem as lista dados


pessoas = [[ 'Pedro', 25], [ 'maria', 19], [ 'João', 32]]

print (pessoas[0][0]) # Pedro
print (pessoas[1][1]) # 19
print (pessoas[2][0]) # João
print (pessoas[1]) # ['Maria', 19] 










