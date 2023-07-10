# Crie um programa que declare uma matriz de dimensão 3x3 
# e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.


"""
import numpy as np

#vetor = np.arange(9)
vetor = np.input (((3, 3))) 


for m in range (1, 10) :
    num = int (input (f'Digite o {m} número da matriz: '))
    #vetor.append (num)

print (vetor)
"""

"""
# MELHOR ATË AGORA
# solução do CHAT GPT solução 1

matriz = []

# Preenchendo a matriz com valores do usuário
for l in range(3):
    linha = []
    for c in range(3):
        valor = int (input ('Digite o valor para a posição [{},{}]: ' .format (l, c)))
        linha.append ([valor])
    matriz.append(f'{linha}')

# Imprimindo a matriz
for linha in matriz:
    print ( f'{linha}' )

"""
import numpy as np

matriz = np.zeros((3,3), dtype=int)

for i in range(3):
    for j in range(3):
        valor = int(input(f"Digite o valor da posição ({i+1},{j+1}): "))
        matriz[i][j] = valor

for linha in matriz:
    print("[", end=" ")
    for valor in linha:
        print(f"[{valor:5d}]", end=", ")
    print("]")


