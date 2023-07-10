#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# 06 de abril



menor = 0
maior = 0

for p in range (1,6) :
    peso = float (input ('Digite o peso da {} pessoa:' .format ( p )))

    #print ('{}' .format(p))
    if p == 1 :
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor :
            menor = peso
        
print ('O menor peso é: {}kg' .format(menor))

print ('O maior peso é: {}kg' .format(maior))

