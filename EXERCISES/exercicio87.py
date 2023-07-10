"""  Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

#even and odd # pares e impares
sunEven = 0
sunOdd = 0 

sunThreeC = 0 
sunThreeL = 0 
maiorC2 = 0 

# PROFESSOR exercicio 86 + minha resolução do exercício
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

for l in range (0, 3) :
    for c in range (0, 3) :
        matriz[l][c] = int (input (f'Digite o valore para {l}, {c}:  '))
        
        if matriz[l][c] % 2 == 0 :
            sunEven += matriz[l][c]
            #print (sunEven)
        elif matriz[l][c] % 2 != 0 :
            sunOdd += matriz[l][c]
            #print (sunOdd)

        if l == 1 :
            if matriz[l][c] > maiorC2 :
                maiorC2 = matriz[l][c]
                print (maiorC2)

        if  l == 2 :
            sunThreeL += matriz[l][c]
            #print (f'Terceira linha: {sunThreeL}')
        
        if  c == 2 :
            sunThreeC += matriz[l][c]
            #print (f'Terceira linha: {sunThreeL}')

print (matriz)

print ('-=' * 30)
for l in range (0, 3) :
    for c in range (0, 3) :
        print (f'[{matriz[l][c]:^5}]', end = '')
    print ()

print (f'Soma pares: {sunEven}')
print (f'Soma impares: {sunOdd}')

print (f'O maior valor da segunda linha é: {maiorC2}')

print (f'Soma terceira coluna: {sunThreeC}')
print (f'Soma terceira linha: {sunThreeL}')

