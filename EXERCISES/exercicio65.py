#  Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

media = 0
resposta = 'S'
cont = 0
maior = 0
menor = 0
soma = 0
while resposta == 'S' :
    
    num = int (input ('Digite um número: '))

    if num == 1 :
        maior = num
        menor = num
    else:
        if num > maior :
            maior = num

        if num < menor:
            menor = num

    resposta = str (input ('Quer continuar? [S/N]: ')).strip().upper()
    cont +=1
    soma = soma + num
    

           
media = (media + soma) / cont
print ('Você digitou {} números e a média foi {:.2f}' .format (cont, media))
print ('O maior número foi {} e o menor foi {}' .format(maior, menor))
