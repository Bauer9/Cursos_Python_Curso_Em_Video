# Crie um programa que declare uma matriz de dimensão 3x3 
# e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

# PROFESSOR
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

for l in range (0, 3) :
    for c in range (0, 3) :
        matriz[l][c] = int (input (f'Digite os valores para {l}, {c}:  '))

print (matriz)

print ('-=' * 30)
for l in range (0, 3) :
    for c in range (0, 3) :
        print (f'[{matriz[l][c]:^5}]', end = '')
    print ()